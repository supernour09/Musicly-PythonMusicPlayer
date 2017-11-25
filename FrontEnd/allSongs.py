# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AllSongs.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from pony.orm import *
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

class Ui_Form(QtGui.QWidget):
    def __init__(self,thePlaylist):
        self.thePlay = thePlaylist
        QtGui.QWidget.__init__(self)
        self.setupUi(self)
        self.populateAllSongs()

    @db_session
    def populateAllSongs(self):
        self.listWidget.clear()
        self.Songs = mDB.viewSong()
        for a in self.Songs:
            self.listWidget.addItem('{:s}'.format(mDB.StringPrepere(a.name)))

    @db_session
    def add(self):
        mDB.addSongToPlaylist(song=self.Songs[self.listWidget.currentRow()].id , playlistId=self.thePlay)
        commit()
        self.close()

    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(400, 300)
        self.verticalLayout_2 = QtGui.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.listWidget = QtGui.QListWidget(Form)
        self.listWidget.setObjectName(_fromUtf8("listView"))
        self.verticalLayout.addWidget(self.listWidget)
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.verticalLayout.addWidget(self.pushButton)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.pushButton.setText(_translate("Form", "Add", None))
        self.pushButton.clicked.connect(self.add)
