# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddNewPlayList.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from Model import MusiclyDB as mDB
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_NewPlayList(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)

    def addNewPlaylist(self , name , desc):
        mDB.set_sql_debug(True)
        mDB.addPlaylist(pName=name, pDesc=desc)
        self.close()

    def setupUi(self, NewPlayList):
        NewPlayList.setObjectName(_fromUtf8("NewPlayList"))
        NewPlayList.resize(400, 300)
        self.verticalLayout_2 = QtGui.QVBoxLayout(NewPlayList)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(NewPlayList)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.textEdit = QtGui.QTextEdit(NewPlayList)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.horizontalLayout.addWidget(self.textEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(NewPlayList)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.textEdit_2 = QtGui.QTextEdit(NewPlayList)
        self.textEdit_2.setObjectName(_fromUtf8("textEdit_2"))
        self.horizontalLayout_2.addWidget(self.textEdit_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.pushButton = QtGui.QPushButton(NewPlayList)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.verticalLayout.addWidget(self.pushButton)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(NewPlayList)
        QtCore.QMetaObject.connectSlotsByName(NewPlayList)

    def retranslateUi(self, NewPlayList):
        NewPlayList.setWindowTitle(_translate("NewPlayList", "New PlayList", None))
        self.label.setText(_translate("NewPlayList", "Name:", None))
        self.label_2.setText(_translate("NewPlayList", "Description :", None))
        self.pushButton.setText(_translate("NewPlayList", "Submit", None))
        self.pushButton.clicked.connect(lambda: self.addNewPlaylist(self.textEdit.toPlainText(),self.textEdit_2.toPlainText()))

