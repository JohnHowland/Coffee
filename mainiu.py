# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainui.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

SCREEN_HEIGHT = int(480)
SCREEN_WIDTH = int(320)

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 320)
        MainWindow.setMaximumSize(QtCore.QSize(480, 320))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        #Buttons
        self.pushButton1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton1.setGeometry(QtCore.QRect(0, 10, 111, 121))
        self.pushButton1.setObjectName("pushButton1")
        self.pushButton2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton2.setGeometry(QtCore.QRect(110, 10, 121, 121))
        self.pushButton2.setObjectName("pushButton2")
        self.pushButton3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton3.setGeometry(QtCore.QRect(230, 10, 121, 121))
        self.pushButton3.setObjectName("pushButton3")
        self.pushButton4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton4.setGeometry(QtCore.QRect(350, 10, 121, 121))
        self.pushButton4.setObjectName("pushButton4")

        #Textedits
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 180, 461, 101))
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")

        #Check Boxes
        self.checkBox1 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox1.setGeometry(QtCore.QRect(30, 150, 62, 17))
        self.checkBox1.setObjectName("checkBox1")
        self.checkBox2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox2.setGeometry(QtCore.QRect(150, 150, 62, 17))
        self.checkBox2.setObjectName("checkBox2")
        self.checkBox3 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox3.setGeometry(QtCore.QRect(270, 150, 62, 17))
        self.checkBox3.setObjectName("checkBox3")
        self.checkBox4 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox4.setGeometry(QtCore.QRect(380, 150, 62, 17))
        self.checkBox4.setObjectName("checkBox4")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 480, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        #Connected the buttons to their callbacks
        self.pushButton1.clicked.connect(self.Button1_callback)
        self.pushButton2.clicked.connect(self.Button2_callback)
        self.pushButton3.clicked.connect(self.Button3_callback)
        self.pushButton4.clicked.connect(self.Button4_callback)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton1.setText(_translate("MainWindow", "Button 1"))
        self.pushButton2.setText(_translate("MainWindow", "Button 2"))
        self.pushButton3.setText(_translate("MainWindow", "Button 3"))
        self.pushButton4.setText(_translate("MainWindow", "Button 4"))

        self.checkBox1.setText(_translate("MainWindow", "Check 1"))
        self.checkBox2.setText(_translate("MainWindow", "Check 2"))
        self.checkBox3.setText(_translate("MainWindow", "Check 3"))
        self.checkBox4.setText(_translate("MainWindow", "Check 4"))

    def Button1_callback(self):
        self.PutMsg("You just called Button1_callback")
        if self.checkBox1.checkState() != 0:
            self.PutMsg("CheckBox 1 is checked!")
        #print(str(c1))

    def Button2_callback(self):
        self.PutMsg("You just called Button2_callback")

    def Button3_callback(self):
        self.PutMsg("You just called Button3_callback")

    def Button4_callback(self):
        self.PutMsg("You just called Button4_callback")


    # def clicked(self, text):
    #     self.label.setText(text)
    #     self.label.adjustSize()
    #     self.PutMsg("Did this show up?")



    def PutMsg(self, text):
        #self.textEdit.setText(text)
        self.textEdit.append(text)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
