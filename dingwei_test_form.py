# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dingwei_test_form.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(838, 461)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.main_layout = QtWidgets.QHBoxLayout()
        self.main_layout.setObjectName("main_layout")
        self.main_cam = QtWidgets.QLabel(self.centralwidget)
        self.main_cam.setText("")
        self.main_cam.setObjectName("main_cam")
        self.main_layout.addWidget(self.main_cam)
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.main_layout.addWidget(self.line_4)
        self.quad_cam = QtWidgets.QGridLayout()
        self.quad_cam.setObjectName("quad_cam")
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.quad_cam.addWidget(self.line_6, 1, 1, 1, 1)
        self.cam_red = QtWidgets.QLabel(self.centralwidget)
        self.cam_red.setText("")
        self.cam_red.setObjectName("cam_red")
        self.quad_cam.addWidget(self.cam_red, 0, 1, 1, 1)
        self.cam_blue = QtWidgets.QLabel(self.centralwidget)
        self.cam_blue.setText("")
        self.cam_blue.setObjectName("cam_blue")
        self.quad_cam.addWidget(self.cam_blue, 2, 1, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.quad_cam.addWidget(self.line_2, 1, 3, 1, 1)
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.quad_cam.addWidget(self.line_3, 2, 2, 1, 1)
        self.cam_yellow = QtWidgets.QLabel(self.centralwidget)
        self.cam_yellow.setText("")
        self.cam_yellow.setObjectName("cam_yellow")
        self.quad_cam.addWidget(self.cam_yellow, 0, 3, 1, 1)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.quad_cam.addWidget(self.line, 0, 2, 1, 1)
        self.cam_green = QtWidgets.QLabel(self.centralwidget)
        self.cam_green.setText("")
        self.cam_green.setObjectName("cam_green")
        self.quad_cam.addWidget(self.cam_green, 2, 3, 1, 1)
        self.main_layout.addLayout(self.quad_cam)
        self.verticalLayout.addLayout(self.main_layout)
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.verticalLayout.addWidget(self.line_5)
        self.Loc_layout = QtWidgets.QGridLayout()
        self.Loc_layout.setObjectName("Loc_layout")
        self.Loc_red = QtWidgets.QTextBrowser(self.centralwidget)
        self.Loc_red.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.Loc_red.setObjectName("Loc_red")
        self.Loc_layout.addWidget(self.Loc_red, 3, 0, 1, 1)
        self.ip_blue_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.ip_blue_edit.setObjectName("ip_blue_edit")
        self.Loc_layout.addWidget(self.ip_blue_edit, 2, 2, 1, 1)
        self.label_blue = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label_blue.setFont(font)
        self.label_blue.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.label_blue.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_blue.setAlignment(QtCore.Qt.AlignCenter)
        self.label_blue.setObjectName("label_blue")
        self.Loc_layout.addWidget(self.label_blue, 0, 2, 1, 1)
        self.label_green_ip = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_green_ip.setFont(font)
        self.label_green_ip.setAlignment(QtCore.Qt.AlignCenter)
        self.label_green_ip.setObjectName("label_green_ip")
        self.Loc_layout.addWidget(self.label_green_ip, 1, 3, 1, 1)
        self.Loc_yellow = QtWidgets.QTextBrowser(self.centralwidget)
        self.Loc_yellow.setObjectName("Loc_yellow")
        self.Loc_layout.addWidget(self.Loc_yellow, 3, 1, 1, 1)
        self.Loc_blue = QtWidgets.QTextBrowser(self.centralwidget)
        self.Loc_blue.setObjectName("Loc_blue")
        self.Loc_layout.addWidget(self.Loc_blue, 3, 2, 1, 1)
        self.ip_red_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.ip_red_edit.setObjectName("ip_red_edit")
        self.Loc_layout.addWidget(self.ip_red_edit, 2, 0, 1, 1)
        self.ip_yellow_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.ip_yellow_edit.setObjectName("ip_yellow_edit")
        self.Loc_layout.addWidget(self.ip_yellow_edit, 2, 1, 1, 1)
        self.label_red_ip = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_red_ip.setFont(font)
        self.label_red_ip.setAlignment(QtCore.Qt.AlignCenter)
        self.label_red_ip.setObjectName("label_red_ip")
        self.Loc_layout.addWidget(self.label_red_ip, 1, 0, 1, 1)
        self.Loc_green = QtWidgets.QTextBrowser(self.centralwidget)
        self.Loc_green.setObjectName("Loc_green")
        self.Loc_layout.addWidget(self.Loc_green, 3, 3, 1, 1)
        self.label_red = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label_red.setFont(font)
        self.label_red.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.label_red.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_red.setAlignment(QtCore.Qt.AlignCenter)
        self.label_red.setObjectName("label_red")
        self.Loc_layout.addWidget(self.label_red, 0, 0, 1, 1)
        self.label_yellow = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label_yellow.setFont(font)
        self.label_yellow.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.label_yellow.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_yellow.setAlignment(QtCore.Qt.AlignCenter)
        self.label_yellow.setObjectName("label_yellow")
        self.Loc_layout.addWidget(self.label_yellow, 0, 1, 1, 1)
        self.label_yellow_ip = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_yellow_ip.setFont(font)
        self.label_yellow_ip.setAlignment(QtCore.Qt.AlignCenter)
        self.label_yellow_ip.setObjectName("label_yellow_ip")
        self.Loc_layout.addWidget(self.label_yellow_ip, 1, 1, 1, 1)
        self.label_blue_ip = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_blue_ip.setFont(font)
        self.label_blue_ip.setAlignment(QtCore.Qt.AlignCenter)
        self.label_blue_ip.setObjectName("label_blue_ip")
        self.Loc_layout.addWidget(self.label_blue_ip, 1, 2, 1, 1)
        self.ip_green_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.ip_green_edit.setObjectName("ip_green_edit")
        self.Loc_layout.addWidget(self.ip_green_edit, 2, 3, 1, 1)
        self.label_green = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label_green.setFont(font)
        self.label_green.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.label_green.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_green.setAlignment(QtCore.Qt.AlignCenter)
        self.label_green.setObjectName("label_green")
        self.Loc_layout.addWidget(self.label_green, 0, 3, 1, 1)
        self.verticalLayout.addLayout(self.Loc_layout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, 0, 0, -1)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_speed = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label_speed.setFont(font)
        self.label_speed.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.label_speed.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_speed.setAlignment(QtCore.Qt.AlignCenter)
        self.label_speed.setObjectName("label_speed")
        self.horizontalLayout.addWidget(self.label_speed)
        self.speed_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.speed_edit.setToolTip("")
        self.speed_edit.setStyleSheet("")
        self.speed_edit.setInputMask("")
        self.speed_edit.setText("")
        self.speed_edit.setObjectName("speed_edit")
        self.horizontalLayout.addWidget(self.speed_edit)
        self.butt_speed_edit = QtWidgets.QPushButton(self.centralwidget)
        self.butt_speed_edit.setObjectName("butt_speed_edit")
        self.horizontalLayout.addWidget(self.butt_speed_edit)
        self.horizontalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.butt_ip_edit = QtWidgets.QPushButton(self.centralwidget)
        self.butt_ip_edit.setObjectName("butt_ip_edit")
        self.horizontalLayout_2.addWidget(self.butt_ip_edit)
        self.butt_start = QtWidgets.QPushButton(self.centralwidget)
        self.butt_start.setObjectName("butt_start")
        self.horizontalLayout_2.addWidget(self.butt_start)
        self.butt_connect = QtWidgets.QPushButton(self.centralwidget)
        self.butt_connect.setObjectName("butt_connect")
        self.horizontalLayout_2.addWidget(self.butt_connect)
        self.butt_end = QtWidgets.QPushButton(self.centralwidget)
        self.butt_end.setObjectName("butt_end")
        self.horizontalLayout_2.addWidget(self.butt_end)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3.setStretch(0, 5)
        self.horizontalLayout_3.setStretch(1, 10)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout.setStretch(0, 15)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 1)
        self.verticalLayout.setStretch(3, 1)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_blue.setText(_translate("MainWindow", "蓝车"))
        self.label_green_ip.setText(_translate("MainWindow", "IP地址"))
        self.label_red_ip.setText(_translate("MainWindow", "IP地址"))
        self.label_red.setText(_translate("MainWindow", "红车"))
        self.label_yellow.setText(_translate("MainWindow", "黄车"))
        self.label_yellow_ip.setText(_translate("MainWindow", "IP地址"))
        self.label_blue_ip.setText(_translate("MainWindow", "IP地址"))
        self.label_green.setText(_translate("MainWindow", "绿车"))
        self.label_speed.setText(_translate("MainWindow", "机器人的速度"))
        self.butt_speed_edit.setText(_translate("MainWindow", "确认修改速度"))
        self.butt_ip_edit.setText(_translate("MainWindow", "确认修改IP"))
        self.butt_start.setText(_translate("MainWindow", "开启位姿计算"))
        self.butt_connect.setText(_translate("MainWindow", "连接服务器"))
        self.butt_end.setText(_translate("MainWindow", "结束"))
