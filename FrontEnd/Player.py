# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Player.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4 import phonon
from Model import MusiclyDB as mDB
from pygame import mixer
from FrontEnd import showSong

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
    def __init__(self, songs):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)
        self.songs = songs
        mixer.init()
        self.populateAllSongs()

    def populateAllSongs(self):
        self.listWidget.clear()
        indx = 0
        for a in self.songs:
            if indx == 0:
                mixer.music.load(a.address)
            else:
                mixer.music.queue(a.address)
            indx = indx +1
            self.listWidget.addItem('{:s}'.format(mDB.StringPrepere(a.name)))

    def play(self):
        mixer.music.play()

    def pause(self):
        mixer.music.stop()

    def showOneSong(self):
        self.tmpList = list(self.songs)
        self.tmpSongData = self.tmpList[self.listWidget.currentRow()]
        self.currSongWindow = showSong.Ui_Form(self.tmpSongData)
        self.currSongWindow.show()

    def deleteOne(self):
        tmplist = list(self.songs)
        currID = tmplist[self.listWidget.currentRow()].id
        mDB.deleteObject(currID, myKey='Song')
        self.close()


    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(657, 370)
        self.verticalLayout_2 = QtGui.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.listWidget = QtGui.QListWidget(Form)
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.verticalLayout.addWidget(self.listWidget)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtGui.QPushButton(Form)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtGui.QPushButton(Form)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton_4 = QtGui.QPushButton(Form)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.horizontalLayout.addWidget(self.pushButton_4)

        self.pushButton_7 = QtGui.QPushButton(Form)
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.horizontalLayout.addWidget(self.pushButton_7)

        self.pushButton_8 = QtGui.QPushButton(Form)
        self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))
        self.horizontalLayout.addWidget(self.pushButton_8)

        self.volumeSlider = phonon.Phonon.VolumeSlider(Form)
        self.volumeSlider.setObjectName(_fromUtf8("volumeSlider"))
        self.horizontalLayout.addWidget(self.volumeSlider)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)


    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Player", None))
        self.pushButton.setText(_translate("Form", "Shuffle", None))
        self.pushButton_2.setText(_translate("Form", "Start", None))
        self.pushButton_2.clicked.connect(self.play)
        self.pushButton_3.setText(_translate("Form", "Stop", None))
        self.pushButton_3.clicked.connect(self.pause)

        self.pushButton_4.setText(_translate("Form", "Delete", None))
        self.pushButton_4.clicked.connect(self.deleteOne)

        self.pushButton_7.setText(_translate("Form", "show song", None))
        self.pushButton_7.clicked.connect(self.showOneSong)

        self.pushButton_8.setText(_translate("Form", "Remove song", None))
        #self.pushButton_8.clicked.connect(self.showOneSong)
