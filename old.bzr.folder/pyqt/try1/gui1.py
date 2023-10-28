# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui1.ui'
#
# Created: Tue Feb 26 14:16:08 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(450, 20, 66, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(100, 20, 66, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.OpenFile = QtGui.QPushButton(self.centralwidget)
        self.OpenFile.setGeometry(QtCore.QRect(520, 510, 98, 27))
        self.OpenFile.setObjectName(_fromUtf8("OpenFile"))
        self.Exit = QtGui.QPushButton(self.centralwidget)
        self.Exit.setGeometry(QtCore.QRect(160, 510, 98, 27))
        self.Exit.setObjectName(_fromUtf8("Exit"))
        self.Run = QtGui.QPushButton(self.centralwidget)
        self.Run.setGeometry(QtCore.QRect(290, 510, 98, 27))
        self.Run.setObjectName(_fromUtf8("Run"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(650, 510, 98, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.button_save = QtGui.QPushButton(self.centralwidget)
        self.button_save.setGeometry(QtCore.QRect(400, 510, 98, 27))
        self.button_save.setObjectName(_fromUtf8("button_save"))
        self.plainTextEdit = QtGui.QTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(350, 40, 431, 451))
        self.plainTextEdit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.plainTextEdit.setLineWrapColumnOrWidth(1)
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.textEdit = QtGui.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 40, 311, 451))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "برنامه", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "خروجی", None, QtGui.QApplication.UnicodeUTF8))
        self.OpenFile.setText(QtGui.QApplication.translate("MainWindow", "باز کردن پرونده", None, QtGui.QApplication.UnicodeUTF8))
        self.Exit.setText(QtGui.QApplication.translate("MainWindow", "خروج", None, QtGui.QApplication.UnicodeUTF8))
        self.Run.setText(QtGui.QApplication.translate("MainWindow", "اجرا", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("MainWindow", "جدید", None, QtGui.QApplication.UnicodeUTF8))
        self.button_save.setText(QtGui.QApplication.translate("MainWindow", "ذخیره", None, QtGui.QApplication.UnicodeUTF8))

