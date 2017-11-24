# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PlayList.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from Model import MusiclyDB as mDB
from FrontEnd import addNewPlayList
from Model.MusiclyDB import *
from pony.orm import *

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

class Ui_PlayList(QtGui.QWidget):

    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)

    def addNewPlayList(self):
        self.addPlayList = addNewPlayList.Ui_NewPlayList();
        self.addPlayList.show()



    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(669, 459)
        self.verticalLayout_2 = QtGui.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.listWidget = QtGui.QListWidget(Form)
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.populateAllPlaylists()
        self.listWidget.show()
        self.verticalLayout.addWidget(self.listWidget)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButton_5 = QtGui.QPushButton(Form)
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.horizontalLayout.addWidget(self.pushButton_5)
        self.pushButton_2 = QtGui.QPushButton(Form)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_3 = QtGui.QPushButton(Form)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    @db_session
    def populateAllPlaylists(self):
        self.playLists = mDB.getAllPlaylists()
        for p in self.playLists:
            print(len(mDB.StringPrepere(p.name)))
            print(len(mDB.StringPrepere(':: Track ::' + str(len(p.songs)))))
            self.listWidget.addItem('{:s}{:s}'.format(mDB.StringPrepere(p.name) ,mDB.StringPrepere(':: Track ::' + str(len(p.songs))) ))


    def showCurrPlaylist(self):
            return self.playLists[self.listWidget.currentRow()]


    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Playlists", None))
        self.pushButton_5.setText(_translate("Form", "Add PlayList", None))
        self.pushButton_5.clicked.connect(self.addNewPlayList)
        self.pushButton_2.setText(_translate("Form", "ٍShow PlayList", None))
        self.pushButton_2.clicked.connect(self.showCurrPlaylist)
        self.pushButton.setText(_translate("Form", "Play", None))
        self.pushButton_3.setText(_translate("Form", "Back", None))
        self.pushButton_3.clicked.connect(self.close)

