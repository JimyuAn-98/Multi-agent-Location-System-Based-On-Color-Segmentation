import math #用于实现一些公式计算
import time #用于实现计时和线程睡眠
import datetime #配合time实现计时
import numpy as np
from cv2 import *
import sys
from dingwei_test_form import Ui_MainWindow #导入UI文件
from PyQt5 import QtGui,QtWidgets,QtCore #Qt核心库
from PyQt5.QtNetwork import QTcpSocket #用于实现Socket通信
from PyQt5.QtCore import QSettings, QObject, QThread #用于实现config文件相关操作和多线程相关操作
from PyQt5.QtGui import QImage,QPixmap,QTextCursor #用于实现界面绘制、视频显示和文本框始终置底
from plug_in import *
import queue #线程之间通信的模块

#定义要写入config文件中的参数
ip_red = None       #红色机器人的ip地址
ip_yellow = None    #黄色机器人的ip地址
ip_blue = None      #蓝色机器人的ip地址
ip_green = None     #绿色机器人的ip地址
speed = "1"         #机器人的移动速度（决定了数据校准每秒钟进行多少次）

#各个颜色的基于HSV色彩空间的阈值信息
lower_red = np.array([130, 43, 46])         #紫色的HSV下限
higher_red = np.array([180, 255, 255])      #紫色的HSV上限
lower_yellow = np.array([26, 65, 65])       #黄色的HSV下限
higher_yellow = np.array([34, 255,255])     #黄色的HSV上限
lower_blue = np.array([100, 50, 50])        #蓝色的HSV下限
higher_blue = np.array([128, 255, 255])     #蓝色的HSV上限
lower_green = np.array([50, 43, 46])        #绿色的HSV下限
higher_green = np.array([90, 255, 255])     #绿色的HSV上限
kernel = np.ones((7, 7), np.uint8)          #腐蚀处理的卷积核大小

#定义颜色分割线程与定位算法线程之间通信的queue
red_queue = queue.LifoQueue()           #Lifo表示后进先出
yellow_queue = queue.LifoQueue()
blue_queue = queue.LifoQueue()
green_queue = queue.LifoQueue()

class Cam_ui(QtWidgets.QMainWindow, Ui_MainWindow):     #程序界面主线程
    def __init__(self, parent = None):      #初始化函数（每一次程序运行时，一定会执行的函数）
        super().__init__(parent)

        self.setupUi(self)

        #初始化槽函数
        self.slot_init()

        #对config文件进行定义
        global ip_red, ip_yellow, ip_blue, ip_green, speed              #对全局变量进行写入
        self.config = QSettings("config.ini", QSettings.IniFormat)      #建立或读取config.ini文件，当程序目录下没有config文件时，建立文件；当目录有已经有config文件时，读取文件
        ip_red = self.config.value("/ip_red/value")                     #从config中建立或读取ip_red的参数
        ip_blue = self.config.value("/ip_blue/value")                   #从config中建立或读取ip_blue的参数
        ip_yellow = self.config.value("/ip_yellow/value")               #从config中建立或读取ip_yellow的参数
        ip_green = self.config.value("/ip_green/value")                 #从config中建立或读取ip_green的参数
        speed = self.config.value("/speed/value")                       #从config中建立或读取speed的参数
        #对speed参数进行判断并显示
        if speed != None:
            self.speed_edit.setText(speed)      #在界面speed_edit中把speed参数值显示出来
            speed = int(speed)                  #config中的参数读取后，得到的是str，需要将其转化为int
            speed = 11-speed                    #speed参数的取值范围是[1,10]
        else:
            self.speed_edit.setText("1")        #当第一次运行程序时，默认speed参数的值为1
            speed = 1
        #在各个对应的文本框中，将ip地址显示出来
        self.ip_red_edit.setText(ip_red)
        self.ip_yellow_edit.setText(ip_yellow)
        self.ip_blue_edit.setText(ip_blue)
        self.ip_green_edit.setText(ip_green)

        #定义定位算法线程
        #PyQt官方推荐使用moveToThread函数来实现多线程，而不是改写Threading中的run()函数
        self.loc = Location(self)
        self.thread_loc = QThread()
        self.loc.moveToThread(self.thread_loc)

        #定义颜色分割线程
        self.camera = Camera(self)
        self.thread_camera = QThread()
        self.camera.moveToThread(self.thread_camera)
        self.thread_camera.started.connect(self.camera.run)     #设置线程执行时，执行的是camera中的run()函数
        self.thread_camera.start()                              #启动线程

        #定义socket通信相关参数
        #定义各个机器人的ip地址和端口
        self.addr_red = (ip_red, 13301)
        self.addr_yellow = (ip_yellow, 13302)
        self.addr_blue = (ip_blue, 13303)
        self.addr_green = (ip_green, 13304)
        #定义各个机器人对应socket
        self.socket_red = socket(AF_INET,SOCK_STREAM)
        self.socket_yellow = socket(AF_INET,SOCK_STREAM)
        self.socket_blue = socket(AF_INET,SOCK_STREAM)
        self.socket_green = socket(AF_INET,SOCK_STREAM)
        #定义默认状态下，socket连接状态为false
        self.connected = False

    def slot_init(self):        #定义槽函数内容（参考Qt的“信号-槽”机制）
        self.butt_ip_edit.clicked.connect(self.ip_info_edit)            #设置ip编辑按钮按下后执行的函数
        self.butt_speed_edit.clicked.connect(self.speed_info_edit)      #设置speed编辑按钮按下后执行的函数
        self.butt_start.clicked.connect(self.dingwei_thread)            #设置定位线程启动按钮按下后执行的函数
        #设置各个文本框的焦点始终置底
        self.loc.cursor_r.connect(self.dw_red)
        self.loc.cursor_y.connect(self.dw_yellow)
        self.loc.cursor_b.connect(self.dw_blue)
        self.loc.cursor_g.connect(self.dw_green)
        self.butt_connect.clicked.connect(self.socket)                  #设置网络通信按钮按下后执行的函数
        self.butt_end.clicked.connect(self.end)                         #设置程序结束按钮按下后执行的函数

    def ip_info_edit(self):
        global ip_red, ip_yellow, ip_blue, ip_green
        #对修改后的ip进行操作
        ipx_red = self.ip_red_edit.text()                       #从文本框中获取修改后的ip地址信息
        if ipx_red != "":                                       #判断修改后的信息是否为空
            self.config.setValue("/ip_red/value", ipx_red)      #修改config文件中对应的值
            ip_red = self.config.value("/ip_red/value")         #重新读取并显示
            self.ip_red_edit.setText(ip_red)

        ipx_yellow = self.ip_yellow_edit.text()
        if ipx_yellow != "":
            self.config.setValue("/ip_yellow/value", ipx_yellow)
            ip_yellow = self.config.value("/ip_yellow/value")
            self.ip_yellow_edit.setText(ip_yellow)

        ipx_blue = self.ip_blue_edit.text()
        if ipx_blue != "":
            self.config.setValue("/ip_blue/value", ipx_blue)
            ip_blue = self.config.value("/ip_blue/value")
            self.ip_blue_edit.setText(ip_blue)

        ipx_green = self.ip_green_edit.text()
        if ipx_green != "":
            self.config.setValue("/ip_green/value", ipx_green)
            ip_green = self.config.value("/ip_green/value")
            self.ip_green_edit.setText(ip_green)

    def speed_info_edit(self):
        global speed
        speedx = self.speed_edit.text()
        if speedx != "":
            self.config.setValue("/speed/value", speedx)
            self.speed_edit.setText(speedx)
            speedx = int(speedx)        #令速度参数的取值为1-10，当速度为10时，参数取1；速度为1时，参数取10
            speed = 11-speedx

    def dw_red(self, red_dis):                          #设置文本框中的文本显示始终聚焦在底部（也就是始终显示最新的一条）
        self.Loc_red.append(red_dis)                    #append表示插入一段字符，并换行
        self.Loc_red.moveCursor(QTextCursor.End)        #将cusor移动到底部
        if self.connected == True:                      #判断Socket是否已经连接
            self.socket_red.send(red_dis.encode())      #通过Socket将字符发送出去，使用默认编码

    def dw_yellow(self, yellow_dis):
        self.Loc_yellow.append(yellow_dis)
        self.Loc_yellow.moveCursor(QTextCursor.End)
        if self.connected == True:
            self.socket_yellow.send(yellow_dis.encode())

    def dw_blue(self, blue_dis):
        self.Loc_blue.append(blue_dis)
        self.Loc_blue.moveCursor(QTextCursor.End)
        if self.connected == True:
            self.socket_blue.send(blue_dis.encode())

    def dw_green(self, green_dis):
        self.Loc_green.append(green_dis)
        self.Loc_green.moveCursor(QTextCursor.End)
        if self.connected == True:
            self.socket_green.send(green_dis.encode())

    def dingwei_thread(self):           #定位算法线程设置
        red_queue.queue.clear()         #将清空queue中的内容清空
        yellow_queue.queue.clear()
        blue_queue.queue.clear()
        green_queue.queue.clear()
        time.sleep(0.5)

        self.thread_loc.started.connect(self.loc.run)       #开启定位算法线程
        self.thread_loc.start()

    def socket(self):                                   #设置Socket通信的连接
        self.socket_red.connect(self.addr_red)
        self.socket_yellow.connect(self.addr_yellow)
        self.socket_blue.connect(self.addr_blue)
        self.socket_green.connect(self.addr_green)
        self.connected = True

    def end(self):                          #程序的结束
        self.socket_red.close()             #关闭Socket
        self.socket_yellow.close()
        self.socket_blue.close()
        self.socket_green.close()
        self.thread_loc.quit()              #关闭线程
        self.thread_camera.quit()
        self.camera.cap.release()           #释放camera
        self.close()                        #关闭界面

class Camera(QObject):              #视频读取与颜色分割线程
    def __init__(self, window, parent = None):
        super().__init__(parent)

        self.core = window                          #令Cam_ui类函数为core，方便调用
        self.cap = cv2.VideoCapture(CAP_DSHOW)      #设置摄像头视频读取，（）中填0会导致程序错误，必须使用CAP_DSHOW
        self.cap.set(3,850)                         #设置
        self.cap.set(4,480)

    def Contrast_and_Brightness(self, contrast, bright, img):               #对画面进行亮度与对比度调节的函数
        blank = np.zeros(img.shape, img.dtype)
        dst = cv2.addWeighted(img, contrast, blank, 1-contrast, bright)
        return dst

    def image(self):
        ret, self.framex = self.cap.read()
        self.frame = self.Contrast_and_Brightness(1.65, 0, self.framex)
        #self.frame = cv2.GaussianBlur(self.frame, (5 ,5), 0)                                                               #高斯滤波
        #self.frame = cv2.medianBlur(self.frame, 3)                                                                         #中值滤波
        self.hsv = cv2.cvtColor(self.frame, cv2.COLOR_BGR2HSV) #BGR->HSV                                                    #颜色空间转换
        show_main = cv2.resize(self.frame,(1280,720))                                                                       #设置界面显示分辨率
        show_main = cv2.cvtColor(self.frame,cv2.COLOR_BGR2RGB)                                                              #将opencv读取的bgr色彩转为rgb
        showImage_main = QtGui.QImage(show_main.data,show_main.shape[1],show_main.shape[0],QtGui.QImage.Format_RGB888)      #对图像重新编码
        self.core.main_cam.setPixmap(QtGui.QPixmap.fromImage(showImage_main))                                               #将图像在界面中显示出来

    def color_red(self):    #紫色的颜色分割和分割后的图像显示
        global rest_red

        #color mask 掩膜
        mask_red = cv2.inRange(self.hsv, lower_red, higher_red)

        #color rest 腐蚀处理
        rest_red = cv2.erode(mask_red, kernel, iterations=1)
        red_queue.put(rest_red)  #将处理后的掩膜放入queue中

        #color res 利用掩膜，对原图像进行与操作
        res_red = cv2.bitwise_and(self.frame,self.frame,mask = mask_red)

        #show images
        image_red = trans_image(res_red)
        self.core.cam_red.setPixmap(QtGui.QPixmap.fromImage(image_red))

    def color_yellow(self):
        global rest_yellow

        #color mask
        mask_yellow = cv2.inRange(self.hsv, lower_yellow, higher_yellow)

        #color rest
        rest_yellow = cv2.erode(mask_yellow, kernel, iterations=1)
        yellow_queue.put(rest_yellow)

        #color res
        res_yellow = cv2.bitwise_and(self.frame,self.frame,mask = mask_yellow)

        #show images
        image_yellow = trans_image(res_yellow)
        self.core.cam_yellow.setPixmap(QtGui.QPixmap.fromImage(image_yellow))

    def color_blue(self):
        #global rest_blue

        #color mask
        mask_blue = cv2.inRange(self.hsv, lower_blue, higher_blue)

        #color rest
        rest_blue = cv2.erode(mask_blue, kernel, iterations=1)
        blue_queue.put(rest_blue)

        #color res
        res_blue = cv2.bitwise_and(self.frame,self.frame,mask = rest_blue)

        #show images
        image_blue = trans_image(res_blue)
        self.core.cam_blue.setPixmap(QtGui.QPixmap.fromImage(image_blue))

    def color_green(self):
        global rest_green

        #color mask
        mask_green = cv2.inRange(self.hsv, lower_green, higher_green)

        #color rest
        rest_green = cv2.erode(mask_green, kernel, iterations=1)
        green_queue.put(rest_green)

        #color res
        res_green = cv2.bitwise_and(self.frame,self.frame,mask = mask_green)

        #show images
        image_green = trans_image(res_green)
        self.core.cam_green.setPixmap(QtGui.QPixmap.fromImage(image_green))

    def run(self):
        while(True):
            print('========================start seg==========================')    #用于统计时间的功能
            t0=time.time()                                                          #读取当前系统时间
            print('seg t0 ',t0)
            self.image()
            self.color_red()
            self.color_yellow()
            self.color_blue()
            self.color_green()

            time.sleep(0.04)
            t1=time.time()
            print('seg t1',t1)
            print("segment time %.6fs"%(t1-t0))

class Location(QObject):            #定位算法
    cursor_r = QtCore.pyqtSignal(str)   #初始化文本框置底的触发信号
    cursor_y = QtCore.pyqtSignal(str)
    cursor_b = QtCore.pyqtSignal(str)
    cursor_g = QtCore.pyqtSignal(str)

    def __init__(self, window, parent = None):
        super().__init__(parent)

    def dingwei(self):                  #定位算法部分
        m_x_r = np.zeros(speed)         #根据速度参数设置空矩阵
        m_y_r = np.zeros(speed)
        m_dir_r = np.zeros(speed)

        m_x_y = np.zeros(speed)
        m_y_y = np.zeros(speed)
        m_dir_y = np.zeros(speed)

        m_x_b = np.zeros(speed)
        m_y_b = np.zeros(speed)
        m_dir_b = np.zeros(speed)

        m_x_g = np.zeros(speed)
        m_y_g = np.zeros(speed)
        m_dir_g = np.zeros(speed)

        for i in range(speed):
            #print('red ', red_queue.qsize())
            red = red_queue.get()               #从queue中取出待处理的数据
            red_queue.task_done()               #取出完成，解除对queue的占用
            x_r, y_r, dir_r = color_loc(red)    #定位算法核心部分
            m_x_r[i] = x_r                      #将计算得到的数据放入空矩阵中，等待数据较正处理
            m_y_r[i] = y_r
            m_dir_r[i] = dir_r

            #print('yellow ',yellow_queue.qsize())
            yellow = yellow_queue.get()
            yellow_queue.task_done()
            x_y, y_y, dir_y = color_loc(yellow)
            m_x_y[i] = x_y
            m_y_y[i] = y_y
            m_dir_y[i] = dir_y

            #print('blue ', blue_queue.qsize())
            blue = blue_queue.get()
            blue_queue.task_done()
            x_b, y_b, dir_b = color_loc(blue)
            m_x_b[i] = x_b
            m_y_b[i] = y_b
            m_dir_b[i] = dir_b

            #print('green ', green_queue.qsize())
            green = green_queue.get()
            green_queue.task_done()
            x_g, y_g, dir_g = color_loc(green)
            m_x_g[i] = x_g
            m_y_g[i] = y_g
            m_dir_g[i] = dir_g

            time.sleep(0.04)

        loc_r, loc_y, loc_b, loc_g = data_analysis(m_x_r, m_y_r, m_dir_r, m_x_y, m_y_y, m_dir_y, m_x_b, m_y_b, m_dir_b, m_x_g, m_y_g, m_dir_g)      #数据较正函数

        self.cursor_r.emit(loc_r)   #触发信号
        self.cursor_y.emit(loc_y)
        self.cursor_b.emit(loc_b)
        self.cursor_g.emit(loc_g)

    def run(self):
        while(1):
            print('====================start loc==========================')
            t0 = time.time()
            print('loc t0 ',t0)
            self.dingwei()
            t1 = time.time()
            print('loc t1 ',t1)
            print("loc time %.6fs"%(t1-t0))

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Cam_ui()
    window.show()
    sys.exit(app.exec_())
