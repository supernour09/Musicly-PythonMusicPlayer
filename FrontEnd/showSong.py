# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'showSong.ui'
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

    def __init__(self, song):
        QtGui.QWidget.__init__(self)
        self.currSong = song
        self.setupUi(self)


    @db_session
    def showSong(self):
        # sName = self.currSong[0]
        # slyrics = self.currSong[1]
        sName = self.currSong.name
        sAlbumName = self.currSong.album.title
        sDate = self.currSong.releaseDate
        sGenre = self.currSong.genres
        sLyrics = self.currSong.lyrics
        self.listWidget.addItem('{:s}'.format('Name : ' + mDB.StringPrepere(sName)))
        self.listWidget.addItem('{:s}'.format('Album : ' + mDB.StringPrepere(sAlbumName)))
        self.listWidget.addItem('{:s}'.format('Release Date : ' + mDB.StringPrepere(sDate)))
        self.listWidget.addItem('{:s}'.format('Genre : ' + mDB.StringPrepere(sGenre)))
        self.listWidget.addItem('{:s}'.format('Lyrics : ' + mDB.StringPrepere(sLyrics)))



    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(400, 251)
        self.verticalLayout_2 = QtGui.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))

        self.listWidget = QtGui.QListWidget(Form)
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.verticalLayout.addWidget(self.listWidget)
        self.showSong()
        self.listWidget.show()

        self.verticalLayout.addLayout(self.horizontalLayout)
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.verticalLayout.addWidget(self.pushButton)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Song Description", None))
        self.pushButton.setText(_translate("Form", "Back", None))
        self.pushButton.clicked.connect(self.close)
