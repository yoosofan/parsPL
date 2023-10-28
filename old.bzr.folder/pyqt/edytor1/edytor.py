# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'edytor.ui'
#
# Created: Sat May  5 18:01:07 2007
#      by: PyQt4 UI code generator 4.1.1
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt4 import QtCore, QtGui

class Ui_notatnik(object):
    def setupUi(self, notatnik):
        notatnik.setObjectName("notatnik")
        notatnik.resize(QtCore.QSize(QtCore.QRect(0,0,560,336).size()).expandedTo(notatnik.minimumSizeHint()))

        self.centralwidget = QtGui.QWidget(notatnik)
        self.centralwidget.setObjectName("centralwidget")

        self.gridlayout = QtGui.QGridLayout(self.centralwidget)
        self.gridlayout.setMargin(9)
        self.gridlayout.setSpacing(6)
        self.gridlayout.setObjectName("gridlayout")

        self.editor_window = QtGui.QTextEdit(self.centralwidget)
        self.editor_window.setObjectName("editor_window")
        self.gridlayout.addWidget(self.editor_window,1,0,1,3)

        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridlayout.addWidget(self.pushButton_2,0,2,1,1)

        self.button_save = QtGui.QPushButton(self.centralwidget)
        self.button_save.setObjectName("button_save")
        self.gridlayout.addWidget(self.button_save,0,1,1,1)

        self.button_open = QtGui.QPushButton(self.centralwidget)
        self.button_open.setObjectName("button_open")
        self.gridlayout.addWidget(self.button_open,0,0,1,1)
        notatnik.setCentralWidget(self.centralwidget)

        self.menubar = QtGui.QMenuBar(notatnik)
        self.menubar.setGeometry(QtCore.QRect(0,0,560,26))
        self.menubar.setObjectName("menubar")
        notatnik.setMenuBar(self.menubar)

        self.statusbar = QtGui.QStatusBar(notatnik)
        self.statusbar.setObjectName("statusbar")
        notatnik.setStatusBar(self.statusbar)

        self.retranslateUi(notatnik)
        QtCore.QObject.connect(self.pushButton_2,QtCore.SIGNAL("clicked()"),notatnik.close)
        QtCore.QMetaObject.connectSlotsByName(notatnik)

    def retranslateUi(self, notatnik):
        notatnik.setWindowTitle(QtGui.QApplication.translate("notatnik", "Notatnik", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("notatnik", "سلام", None, QtGui.QApplication.UnicodeUTF8))
        self.button_save.setText(QtGui.QApplication.translate("notatnik", "خدانگهدار", None, QtGui.QApplication.UnicodeUTF8))
        self.button_open.setText(QtGui.QApplication.translate("notatnik", "برو بیرون Plik", None, QtGui.QApplication.UnicodeUTF8))

