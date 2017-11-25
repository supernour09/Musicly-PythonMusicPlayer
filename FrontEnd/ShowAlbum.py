# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ShowAlbums.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from pony.orm import db_session
from FrontEnd import addAlbum,Player
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

class Ui_ShowAlbum(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)


    def openAddAlbum(self):
        self.addAlbum = addAlbum.Ui_Form();
        self.addAlbum.show()

    @db_session
    def populateAllAlbums(self):
        self.listWidget.clear()
        self.albums = mDB.viewAlbums()
        for a in self.albums:
            self.listWidget.addItem('{:s}{:s}'.format(mDB.StringPrepere(a.title), mDB.StringPrepere(':: Track ::' + str(len(a.songs)))))

    def deleteOne(self):
        currID = self.albums[self.listWidget.currentRow()].id
        mDB.deleteObject(currID, myKey='Album')
        self.populateAllAlbums()




    def play(self):
        self.player = Player.Ui_Form(self.albums[self.listWidget.currentRow()].songs)
        self.player.show()


    def setupUi(self, ShowAlbum):
        ShowAlbum.setObjectName(_fromUtf8("ShowAlbum"))
        ShowAlbum.resize(680, 459)
        self.verticalLayout_2 = QtGui.QVBoxLayout(ShowAlbum)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.listWidget = QtGui.QListWidget(ShowAlbum)
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.verticalLayout.addWidget(self.listWidget)
        self.populateAllAlbums()
        self.listWidget.show()
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButton_5 = QtGui.QPushButton(ShowAlbum)
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.horizontalLayout.addWidget(self.pushButton_5)
        self.pushButton = QtGui.QPushButton(ShowAlbum)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_6 = QtGui.QPushButton(ShowAlbum)
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.horizontalLayout.addWidget(self.pushButton_6)
        self.pushButton_8 = QtGui.QPushButton(ShowAlbum)
        self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))
        self.horizontalLayout.addWidget(self.pushButton_8)
        self.pushButton_3 = QtGui.QPushButton(ShowAlbum)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(ShowAlbum)
        QtCore.QMetaObject.connectSlotsByName(ShowAlbum)

    def retranslateUi(self, ShowAlbum):
        ShowAlbum.setWindowTitle(_translate("ShowAlbum", "Album", None))
        self.pushButton_5.setText(_translate("ShowAlbum", "Add Album", None))
        self.pushButton_5.clicked.connect(self.openAddAlbum)
        self.pushButton.setText(_translate("ShowAlbum", "Play", None))
        self.pushButton.clicked.connect(self.play)
        self.pushButton_3.setText(_translate("ShowAlbum", "Back", None))
        self.pushButton_3.clicked.connect(self.close)
        self.pushButton_6.setText(_translate("ShowGenre", "Refresh", None))
        self.pushButton_6.clicked.connect(self.populateAllAlbums)
        self.pushButton_8.setText(_translate("ShowGenre", "Delete", None))
        self.pushButton_8.clicked.connect(self.deleteOne)
