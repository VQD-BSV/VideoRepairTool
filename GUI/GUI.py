# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt6 UI code generator 6.5.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(713, 261)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Logo/logo.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_Copyright = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_Copyright.setGeometry(QtCore.QRect(10, 230, 281, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        self.label_Copyright.setFont(font)
        self.label_Copyright.setText("")
        self.label_Copyright.setObjectName("label_Copyright")
        self.Browse_Path = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.Browse_Path.setGeometry(QtCore.QRect(10, 10, 381, 101))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Browse_Path.setFont(font)
        self.Browse_Path.setObjectName("Browse_Path")
        self.Open_File = QtWidgets.QPushButton(parent=self.Browse_Path)
        self.Open_File.setGeometry(QtCore.QRect(330, 20, 42, 25))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        self.Open_File.setFont(font)
        self.Open_File.setObjectName("Open_File")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.Browse_Path)
        self.lineEdit.setGeometry(QtCore.QRect(10, 20, 311, 24))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lineEdit.setFont(font)
        self.lineEdit.setAcceptDrops(True)
        self.lineEdit.setAccessibleDescription("")
        self.lineEdit.setAutoFillBackground(False)
        self.lineEdit.setStyleSheet("border-radius: 4px;  border: 0.5px solid black;")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.Browse_Path)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 60, 311, 24))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("border-radius: 4px;  border: 0.5px solid black;")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.Open_File_2 = QtWidgets.QPushButton(parent=self.Browse_Path)
        self.Open_File_2.setGeometry(QtCore.QRect(330, 60, 42, 25))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        self.Open_File_2.setFont(font)
        self.Open_File_2.setObjectName("Open_File_2")
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(400, 10, 301, 211))
        self.groupBox.setObjectName("groupBox")
        self.textEdit = QtWidgets.QTextEdit(parent=self.groupBox)
        self.textEdit.setGeometry(QtCore.QRect(10, 20, 281, 181))
        self.textEdit.setObjectName("textEdit")
        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 110, 381, 111))
        self.groupBox_2.setObjectName("groupBox_2")
        self.b_Start = QtWidgets.QPushButton(parent=self.groupBox_2)
        self.b_Start.setGeometry(QtCore.QRect(10, 70, 361, 26))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(True)
        self.b_Start.setFont(font)
        self.b_Start.setObjectName("b_Start")
        MainWindow.setCentralWidget(self.centralwidget)
        self.actionSave_AS = QtGui.QAction(parent=MainWindow)
        self.actionSave_AS.setObjectName("actionSave_AS")
        self.Open_File1 = QtGui.QAction(parent=MainWindow)
        self.Open_File1.setObjectName("Open_File1")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "VideoRepair v1.0.0"))
        self.Browse_Path.setTitle(_translate("MainWindow", "Browse Path"))
        self.Open_File.setText(_translate("MainWindow", "..."))
        self.lineEdit.setText(_translate("MainWindow", "                         Corrupted/Encrypted File"))
        self.lineEdit_2.setText(_translate("MainWindow", "                                    Reference File"))
        self.Open_File_2.setText(_translate("MainWindow", "..."))
        self.groupBox.setTitle(_translate("MainWindow", "Logs"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Op"))
        self.b_Start.setText(_translate("MainWindow", "START"))
        self.actionSave_AS.setText(_translate("MainWindow", "Save As"))
        self.Open_File1.setText(_translate("MainWindow", "Open File"))
