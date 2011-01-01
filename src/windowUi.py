# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Sat Jan 01 05:58:26 2011
#      by: PyQt4 UI code generator 4.8.2
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
        MainWindow.resize(297, 362)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.linePlayer = QtGui.QLineEdit(self.centralwidget)
        self.linePlayer.setGeometry(QtCore.QRect(10, 10, 113, 20))
        self.linePlayer.setObjectName(_fromUtf8("linePlayer"))
        self.comboPlatform = QtGui.QComboBox(self.centralwidget)
        self.comboPlatform.setGeometry(QtCore.QRect(130, 10, 69, 22))
        self.comboPlatform.setObjectName(_fromUtf8("comboPlatform"))
        self.comboPlatform.addItem(_fromUtf8(""))
        self.comboPlatform.addItem(_fromUtf8(""))
        self.comboPlatform.addItem(_fromUtf8(""))
        self.btnGo = QtGui.QPushButton(self.centralwidget)
        self.btnGo.setGeometry(QtCore.QRect(210, 10, 75, 23))
        self.btnGo.setObjectName(_fromUtf8("btnGo"))
        self.treeComingUp = QtGui.QTreeView(self.centralwidget)
        self.treeComingUp.setGeometry(QtCore.QRect(10, 40, 271, 281))
        self.treeComingUp.setObjectName(_fromUtf8("treeComingUp"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 297, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuBCS = QtGui.QMenu(self.menubar)
        self.menuBCS.setObjectName(_fromUtf8("menuBCS"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuBCS.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.linePlayer.setText(QtGui.QApplication.translate("MainWindow", "VelocityGirl", None, QtGui.QApplication.UnicodeUTF8))
        self.comboPlatform.setItemText(0, QtGui.QApplication.translate("MainWindow", "PC", None, QtGui.QApplication.UnicodeUTF8))
        self.comboPlatform.setItemText(1, QtGui.QApplication.translate("MainWindow", "360", None, QtGui.QApplication.UnicodeUTF8))
        self.comboPlatform.setItemText(2, QtGui.QApplication.translate("MainWindow", "PS3", None, QtGui.QApplication.UnicodeUTF8))
        self.btnGo.setText(QtGui.QApplication.translate("MainWindow", "Go", None, QtGui.QApplication.UnicodeUTF8))
        self.menuBCS.setTitle(QtGui.QApplication.translate("MainWindow", "BCS", None, QtGui.QApplication.UnicodeUTF8))

