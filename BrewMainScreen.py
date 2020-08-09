# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BrewMainScreen.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from clock import *
from hardware_interface import*

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.clk = clock()
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 320)
        font = QtGui.QFont()
        font.setPointSize(16)
        MainWindow.setFont(font)
        self.brew = 0

        # setting background image to status bar 
        #MainWindow.statusBar().setStyleSheet("background-image : url(beans.jpg);")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        #background Photo
        self.BackgroundPhoto = QtWidgets.QGraphicsView(self.centralwidget)
        self.BackgroundPhoto.setGeometry(QtCore.QRect(0, 0, 480, 320))
        self.BackgroundPhoto.setAutoFillBackground(False)
        self.BackgroundPhoto.setObjectName("BackgroundPhoto")
        self.BackgroundPhoto.setStyleSheet("background-image : url(beans.jpg);")

        #Clock
        self.ClockLabel = QtWidgets.QLabel(self.centralwidget)
        self.ClockLabel.setGeometry(QtCore.QRect(80, 150, 310, 101))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(40)
        self.ClockLabel.setFont(font)
        self.ClockLabel.setStyleSheet("color: white")
        self.ClockLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ClockLabel.setObjectName("ClockLabel")

        #On/Off Button
        self.on_offButton = QtWidgets.QPushButton(self.centralwidget)
        self.on_offButton.setGeometry(QtCore.QRect(20, 20, 180, 125))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.on_offButton.setFont(font)
        self.on_offButton.setObjectName("on_offButton")

        #Brew Button
        self.brewButton = QtWidgets.QPushButton(self.centralwidget)
        self.brewButton.setGeometry(QtCore.QRect(280, 20, 180, 125))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.brewButton.setFont(font)
        self.brewButton.setObjectName("brewButton")

        #Clock Test Button
        self.clockTest = QtWidgets.QPushButton(self.centralwidget)
        self.clockTest.setGeometry(QtCore.QRect(20, 260, 150, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.clockTest.setFont(font)
        self.clockTest.setObjectName("clockTest")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #Connected the buttons to their callbacks
        self.on_offButton.clicked.connect(self.on_off_callback)
        self.brewButton.clicked.connect(self.brew_callback)
        self.clockTest.clicked.connect(self.clockTest_callback)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.ClockLabel.setText(_translate("MainWindow", "12:00"))
        self.on_offButton.setText(_translate("MainWindow", "On/Off"))
        self.brewButton.setText(_translate("MainWindow", "Brew"))
        self.clockTest.setText(_translate("MainWindow", "Clk test"))

    def on_off_callback(self):
        pass

    def brew_callback(self):
        if self.brew == 0:
            lll.setPinState(1)
        elif self.brew == 1:
            lll.setPinState(0)

    def clockTest_callback(self):
        txt = self.clk.getCurrentTime()
        print(str(txt))
        self.ClockLabel.setText(str(txt))

if __name__ == "__main__":
    import sys
    lll = pin_class(17)
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
