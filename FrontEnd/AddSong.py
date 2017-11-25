# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddSong.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from pony.orm import *
from Model import MusiclyDB as mDB
import tkinter as tk
from tkinter import filedialog

from pony.orm import db_session

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

class Ui_AddSong(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)


    def getFile(self):
        fileName = QtGui.QFileDialog.getOpenFileName(self, 'OpenFile')
        self.lineEdit_2.setText(fileName)
        print(fileName)

    @db_session
    def addTheSong(self):
        sName = self.lineEdit.text()
        sAddress = self.lineEdit_2.text()
        sArtist = self.lineEdit_10.text()
        sArtistFt = self.lineEdit_5.text()
        sBand = self.lineEdit_9.text()
        sAlbum = self.lineEdit_6.text()
        sDesc = self.lineEdit_3.text()
        sGenre = self.lineEdit_4.text()
        sLyrics = self.lineEdit_8.text()
        sDate = self.lineEdit_7.text()
        song = mDB.Song(name = sName ,address = sAddress , lyrics =sLyrics ,releaseDate=sDate,genres=sGenre )
        tmpBandId = 0
        if sBand is not None:
            isExistBand = select(c for c in mDB.Band if c.name is sBand)
            if len(isExistBand) == 0:
                newBand = mDB.addBand(aName=sBand)
                newBand.songs.add(song)
                tmpBandId = newBand.id
            else:
                isExistBand.first().songs.add(song)
                tmpBandId = isExistBand.first().id

        if sArtist is not None:
            isExistArtisit = select(c for c in mDB.Artist if c.name is sArtist)
            if len(isExistArtisit) == 0:
                newArtisit = mDB.addArtist(aName=sArtist)
                newArtisit.songs.add(song)
                mDB.Band[tmpBandId].artists.add(newArtisit)
            else:
                isExistArtisit.first().songs.add(song)
                mDB.Band[tmpBandId].artists.add(isExistArtisit)

        if sArtistFt is not None:
            isExistArtisitFt = select(c for c in mDB.Artist if c.name is sArtist)
            if len(isExistArtisitFt) == 0:
                newArtisit = mDB.addArtist(aName=sArtistFt)
                newArtisit.songs.add(song)
                song.artists.add(isExistArtisitFt)
            else:
                isExistArtisitFt.first().songs.add(song)
                song.artists.add(isExistArtisitFt)


        if sAlbum is not None:
            isExistAlbum = select(c for c in mDB.Album if c.title is sAlbum)
            if len(isExistAlbum) == 0:
                newAlbum = mDB.addAlbum(aTitle=sAlbum , BandId = tmpBandId )
                newAlbum.songs.add(song)
            else:
                isExistAlbum.first().songs.add(song)



        self.close()


    def setupUi(self, AddSong):
        AddSong.setObjectName(_fromUtf8("AddSong"))
        AddSong.resize(657, 414)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        AddSong.setFont(font)
        self.verticalLayout_2 = QtGui.QVBoxLayout(AddSong)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.label_7 = QtGui.QLabel(AddSong)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setTextFormat(QtCore.Qt.RichText)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_7.addWidget(self.label_7)
        self.lineEdit = QtGui.QLineEdit(AddSong)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout_7.addWidget(self.lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(AddSong)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setWordWrap(False)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit_2 = QtGui.QLineEdit(AddSong)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.horizontalLayout.addWidget(self.lineEdit_2)
        self.pushButton = QtGui.QPushButton(AddSong)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(AddSong)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setTextFormat(QtCore.Qt.RichText)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEdit_3 = QtGui.QLineEdit(AddSong)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.horizontalLayout_2.addWidget(self.lineEdit_3)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_3 = QtGui.QLabel(AddSong)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setTextFormat(QtCore.Qt.RichText)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_3.addWidget(self.label_3)
        self.lineEdit_4 = QtGui.QLineEdit(AddSong)
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.horizontalLayout_3.addWidget(self.lineEdit_4)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.label_10 = QtGui.QLabel(AddSong)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setTextFormat(QtCore.Qt.RichText)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.horizontalLayout_10.addWidget(self.label_10)
        self.lineEdit_10 = QtGui.QLineEdit(AddSong)
        self.lineEdit_10.setObjectName(_fromUtf8("lineEdit_10"))
        self.horizontalLayout_10.addWidget(self.lineEdit_10)
        self.verticalLayout.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.label_8 = QtGui.QLabel(AddSong)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setTextFormat(QtCore.Qt.RichText)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.horizontalLayout_8.addWidget(self.label_8)
        self.lineEdit_5 = QtGui.QLineEdit(AddSong)
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.horizontalLayout_8.addWidget(self.lineEdit_5)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_5 = QtGui.QLabel(AddSong)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setTextFormat(QtCore.Qt.RichText)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_5.addWidget(self.label_5)
        self.lineEdit_6 = QtGui.QLineEdit(AddSong)
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
        self.horizontalLayout_5.addWidget(self.lineEdit_6)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_6 = QtGui.QLabel(AddSong)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setTextFormat(QtCore.Qt.RichText)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_6.addWidget(self.label_6)
        self.lineEdit_7 = QtGui.QLineEdit(AddSong)
        self.lineEdit_7.setObjectName(_fromUtf8("lineEdit_7"))
        self.horizontalLayout_6.addWidget(self.lineEdit_7)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.label_9 = QtGui.QLabel(AddSong)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setTextFormat(QtCore.Qt.RichText)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.horizontalLayout_9.addWidget(self.label_9)
        self.lineEdit_8 = QtGui.QLineEdit(AddSong)
        self.lineEdit_8.setObjectName(_fromUtf8("lineEdit_8"))
        self.horizontalLayout_9.addWidget(self.lineEdit_8)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_4 = QtGui.QLabel(AddSong)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setTextFormat(QtCore.Qt.RichText)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_4.addWidget(self.label_4)
        self.lineEdit_9 = QtGui.QLineEdit(AddSong)
        self.lineEdit_9.setObjectName(_fromUtf8("lineEdit_9"))
        self.horizontalLayout_4.addWidget(self.lineEdit_9)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.pushButton_2 = QtGui.QPushButton(AddSong)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.verticalLayout.addWidget(self.pushButton_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(AddSong)
        QtCore.QMetaObject.connectSlotsByName(AddSong)

    def retranslateUi(self, AddSong):
        AddSong.setWindowTitle(_translate("AddSong", "Add Song", None))
        self.label_7.setText(_translate("AddSong", "Name :", None))
        self.label.setText(_translate("AddSong", "song", None))
        self.pushButton.setText(_translate("AddSong", "Browse", None))
        self.label_2.setText(_translate("AddSong", "Description:", None))
        self.label_3.setText(_translate("AddSong", "Genre :", None))
        self.label_10.setText(_translate("AddSong", "Artist :", None))
        self.label_8.setText(_translate("AddSong", "Featured Artist :", None))
        self.label_5.setText(_translate("AddSong", "Album :", None))
        self.label_6.setText(_translate("AddSong", "Relase Date :", None))
        self.label_9.setText(_translate("AddSong", "Lyrics", None))
        self.label_4.setText(_translate("AddSong", "Band :", None))
        self.pushButton_2.setText(_translate("AddSong", "Submit", None))
        self.pushButton.clicked.connect(self.getFile)
        self.pushButton_2.clicked.connect(self.addTheSong)