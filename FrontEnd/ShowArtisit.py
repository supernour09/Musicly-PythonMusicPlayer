# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ShowArtisit.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from pony.orm import *
from FrontEnd import addArtist , Player
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


class Ui_Artisit(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)

    def openAddArtist(self):
        self.addArtist = addArtist.Ui_Form();
        self.addArtist.show()

    @db_session
    def populateAllArtists(self):
        self.listWidget.clear()
        self.artists = mDB.viewArtists()
        print(self.artists[0].songs)
        for a in self.artists:
            self.listWidget.addItem('{:s}'.format(mDB.StringPrepere(a.name)))
            # QListWidgetItem = QtGui.QListWidgetItem()
            # QListWidgetItem.setData(5, a.id)
            # QListWidgetItem.setText('{:s}'.format(mDB.StringPrepere(a.name)))
            # s = 'i = ' + str(i) + ' mainId = ' + str(a.id) + ' dataId = ' + str(QListWidgetItem.data(5)) + ' Text = ' + QListWidgetItem.text()
            # print(s)
            # i += 1
            # self.listWidget.addItem(QListWidgetItem)

    def play(self):
        self.player = list(mDB.Song.select(lambda s: s.artis > 100))
        self.player.show()

    def deleteOne(self):
        currID = self.artists[self.listWidget.currentRow()].id
        mDB.deleteObject(currID, myKey='Artist')
        self.populateAllArtists()

    def setupUi(self, Artisit):
        Artisit.setObjectName(_fromUtf8("Artisit"))
        Artisit.resize(670, 459)
        self.verticalLayout_2 = QtGui.QVBoxLayout(Artisit)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.listWidget = QtGui.QListWidget(Artisit)
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.verticalLayout.addWidget(self.listWidget)
        self.populateAllArtists()
        self.listWidget.show()
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButton_5 = QtGui.QPushButton(Artisit)
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.horizontalLayout.addWidget(self.pushButton_5)
        self.pushButton = QtGui.QPushButton(Artisit)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_6 = QtGui.QPushButton(Artisit)
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.horizontalLayout.addWidget(self.pushButton_6)
        self.pushButton_8 = QtGui.QPushButton(Artisit)
        self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))
        self.horizontalLayout.addWidget(self.pushButton_8)
        self.pushButton_3 = QtGui.QPushButton(Artisit)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Artisit)
        QtCore.QMetaObject.connectSlotsByName(Artisit)




    def retranslateUi(self, Artisit):
        Artisit.setWindowTitle(_translate("Artisit", "Artists", None))
        self.pushButton_5.setText(_translate("Artisit", "Add Artist", None))
        self.pushButton_5.clicked.connect(self.openAddArtist)
        self.pushButton.setText(_translate("Artisit", "Play", None))
        self.pushButton.clicked.connect(self.play)
        self.pushButton_3.setText(_translate("Artisit", "Back", None))
        self.pushButton_3.clicked.connect(self.close)
        self.pushButton_6.setText(_translate("ShowGenre", "Refresh", None))
        self.pushButton_6.clicked.connect(self.populateAllArtists)
        self.pushButton_8.setText(_translate("ShowGenre", "Delete", None))
        self.pushButton_8.clicked.connect(self.deleteOne)
