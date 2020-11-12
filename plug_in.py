import cv2
from cv2 import *
import sys
import math
import numpy as np
from PyQt5 import QtGui
from PyQt5.QtGui import QImage

def trans_image(res_color):     #视频图像转换函数，从opencv格式转换为qt可以使用的格式
        show = cv2.resize(res_color,(240,135))
        show = cv2.cvtColor(show,cv2.COLOR_BGR2RGB)
        showImage = QtGui.QImage(show.data,show.shape[1],show.shape[0],QtGui.QImage.Format_RGB888)

        return showImage

def data_analysis(x_r, y_r, dir_r, x_y, y_y, dir_y, x_b, y_b, dir_b, x_g, y_g, dir_g):  #数据较正函数

    #这当中的角度校正算法其实还有一点问题，我只考虑了当紫色色块的角度为钝角时的校正计算，没有考虑锐角。。。。。

    x_r = x_r[x_r != 0]         #将矩阵中的为0的数据剔除
    y_r = y_r[y_r != 0]
    dir_r = dir_r[dir_r != 0]
    mean_x_r = np.mean(x_r)     #取平均值
    mean_y_r = np.mean(y_r)
    mean_dir_r = np.mean(dir_r)
    matrix_x_r = x_r[np.abs(x_r - mean_x_r) <= 10]      #进行3希格玛判断，剔除坏值
    matrix_y_r = y_r[np.abs(y_r - mean_y_r) <= 10]
    matrix_dir_r = dir_r[np.abs(dir_r - mean_dir_r) <= 10]
    loc_r = [np.mean(matrix_x_r), np.mean(matrix_y_r), np.mean(matrix_dir_r)]   #将剩余数据取平均值
    loc_r = np.array(loc_r)
    beta = 90 + loc_r[2]
    #print(loc_r)

    x_y = x_y[x_y != 0]
    y_y = y_y[y_y != 0]
    dir_y = dir_y[dir_y != 0]
    mean_x_y = np.mean(x_y)
    mean_y_y = np.mean(y_y)
    mean_dir_y = np.mean(dir_y)
    matrix_x_y = x_y[np.abs(x_y - mean_x_y) <= 10]
    matrix_y_y = y_y[np.abs(y_y - mean_y_y) <= 10]
    matrix_dir_y = dir_y[np.abs(dir_y - mean_dir_y) <= 10]
    loc_y = [np.mean(matrix_x_y), np.mean(matrix_y_y), np.mean(matrix_dir_y)]
    loc_y = np.array(loc_y)
    loc_y[0] = loc_y[0] - loc_r[0]
    loc_y[1] = loc_r[1] - loc_y[1]
    if loc_y[2] >= 0:
        loc_y[2] = loc_y[2] - beta
    else:
        loc_y[2] = 90 + loc_y[2] - loc_r[2]

    x_b = x_b[x_b != 0]
    y_b = y_b[y_b != 0]
    dir_b = dir_b[dir_b != 0]
    mean_x_b = np.mean(x_b)
    mean_y_b = np.mean(y_b)
    mean_dir_b = np.mean(dir_b)
    matrix_x_b = x_b[np.abs(x_b - mean_x_b) <= 10]
    matrix_y_b = y_b[np.abs(y_b - mean_y_b) <= 10]
    matrix_dir_b = dir_b[np.abs(dir_b - mean_dir_b) <= 10]
    loc_b = [np.mean(matrix_x_b), np.mean(matrix_y_b), np.mean(matrix_dir_b)]
    loc_b = np.array(loc_b)
    loc_b[0] = loc_b[0] - loc_r[0]
    loc_b[1] = loc_r[1] - loc_b[1]
    if loc_b[2] >= 0:
        loc_b[2] = loc_b[2] - beta
    else:
        loc_b[2] = 90 + loc_b[2] - loc_r[2]

    x_g = x_g[x_g != 0]
    y_g = y_g[y_g != 0]
    dir_g = dir_g[dir_g != 0]
    mean_x_g = np.mean(x_g)
    mean_y_g = np.mean(y_g)
    mean_dir_g = np.mean(dir_g)
    matrix_x_g = x_g[np.abs(x_g - mean_x_g) <= 10]
    matrix_y_g = y_g[np.abs(y_g - mean_y_g) <= 10]
    matrix_dir_g = dir_g[np.abs(dir_g - mean_dir_g) <= 10]
    loc_g = [np.mean(matrix_x_g), np.mean(matrix_y_g), np.mean(matrix_dir_g)]
    loc_g = np.array(loc_g)
    loc_g[0] = loc_g[0] - loc_r[0]
    loc_g[1] = loc_r[1] - loc_g[1]
    if loc_g[2] >= 0:
        loc_g[2] = loc_g[2] - beta
    else:
        loc_g[2] = 90 + loc_g[2] - loc_r[2]

    loc_r = '%.f - %.f - %.f'%(loc_r[0], loc_r[1], loc_r[2])    #将数组中的数据转化为字符串
    loc_y = '%.f - %.f - %.f'%(loc_y[0], loc_y[1], loc_y[2])
    loc_b = '%.f - %.f - %.f'%(loc_b[0], loc_b[1], loc_b[2])
    loc_g = '%.f - %.f - %.f'%(loc_g[0], loc_g[1], loc_g[2])

    return str(loc_r), str(loc_y), str(loc_b), str(loc_g)

def color_loc(rest_color):
    #bianyuan = cv2.Canny(rest_color, 1, 1, 5) Canny算法，效果不明显
    countors, hierachy = cv2.findContours(rest_color, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)     #cv.contours是用于有关图像中轮廓的函数
    #print(countors)
    number = len(countors)      #计算轮廓个数，我这里每种颜色用了两个，一大一小，用于判断车体方向
    #print(number)
    if number <= 1:     #如果轮廓个数为零（即图像中没有符合条件的内容），则输出位置和角度为零
        cx = 0
        cy = 0
        dir = 0
        #diry = 0
    else:
        i_final = []        #用来存储各个轮廓的面积的数组
        for i in range(number):      #根据轮廓数量进行循环执行
            cnt = countors[i]
            M = cv2.moments(cnt)        #moments是用于计算图像矩
            a = M['m00']        #m00对应的参数是这个块的面积
            #print(a)
            #if a != 0.0:
            i_final.append(a)       #在i_final数组中插入获取的当前轮廓的面积
        #print(i_final)
        if len(i_final)<2:      #如果i_final中记录的值的数量小于2，则输出位置和角度置零
            cx = 0
            cy = 0
            dir = 0
            #diry = 0
        else:
            #定位不准和颜色分割效果不够好有很大关系！！！！
            paixu = sorted(range(len(i_final)), key=lambda k: i_final[k])
            max_index = paixu[-1]
            sec_index = paixu[-2]
            #print(max_index,sec_index)
            cnt_0 = countors[max_index]     #big one    选取到的最大两个算出位置坐标与方向向量
            cnt_1 = countors[sec_index]     #small one
            #print(cnt_0)
            M_0 = cv2.moments(cnt_0)        #分别计算二者的图像矩
            M_1 = cv2.moments(cnt_1)
            #print(M_0['m00'],M_1['m00'])
            cx_0 = int(M_0['m10'] / M_0['m00'])     #大的轮廓（色块）的中心图像坐标的值
            cy_0 = int(M_0['m01'] / M_0['m00'])

            cx_1 = int(M_1['m10'] / M_1['m00'])     #小的轮廓（色块）的中心图像坐标的值
            cy_1 = int(M_1['m01'] / M_1['m00'])
            cx = (cx_0 + cx_1) / 2
            cy = (cy_0 + cy_1) / 2
            #print(cx_0, cx_1, cy_0, cy_1)
            #rad = angle * (math.pi/180)
            #cy = cy/(math.asin(rad))
            dirx = cx_1 - cx_0
            diry = cy_0 - cy_1
            #print(dirx, diry)
            #diry = diry/(math.asin(rad))
            dir = math.atan(diry/dirx)
            dir = (180*dir)/3.1415926       #这样算出来钝角为负数，锐角为正数
            #print(dir)
            #print(cx,cy,dirx,diry)

    return cx, cy, dir
