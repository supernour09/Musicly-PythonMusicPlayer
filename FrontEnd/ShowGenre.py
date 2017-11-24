# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ShowGenre.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from pony.orm import db_session
from Model import MusiclyDB as mDB
from FrontEnd import addGenre

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

class Ui_ShowGenre(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)

    @db_session
    def populateAllGenres(self):
        self.listWidget.clear()
        self.genres = mDB.viewGenres()
        list = []
        for g in self.genres:
            if g.name not in list:
                list.append(g.name)
                self.listWidget.addItem('{:s}'.format(mDB.StringPrepere(g.name)))


    def openAddGenre(self):
        self.addGenre = addGenre.Ui_Form();
        self.addGenre.show()


    #TODO: create addGenre Function



    def setupUi(self, ShowGenre):
        ShowGenre.setObjectName(_fromUtf8("ShowGenre"))
        ShowGenre.resize(683, 480)
        self.verticalLayout_2 = QtGui.QVBoxLayout(ShowGenre)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.listWidget = QtGui.QListWidget(ShowGenre)
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.verticalLayout.addWidget(self.listWidget)
        self.populateAllGenres()
        self.listWidget.show()
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButton_5 = QtGui.QPushButton(ShowGenre)
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.horizontalLayout.addWidget(self.pushButton_5)
        self.pushButton = QtGui.QPushButton(ShowGenre)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_6 = QtGui.QPushButton(ShowGenre)
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.horizontalLayout.addWidget(self.pushButton_6)
        self.pushButton_3 = QtGui.QPushButton(ShowGenre)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(ShowGenre)
        QtCore.QMetaObject.connectSlotsByName(ShowGenre)

    def retranslateUi(self, ShowGenre):
        ShowGenre.setWindowTitle(_translate("ShowGenre", "Genre", None))
        self.pushButton_5.setText(_translate("ShowGenre", "Add Genre", None))
        self.pushButton_5.clicked.connect(self.openAddGenre)
        self.pushButton.setText(_translate("ShowGenre", "Play", None))
        self.pushButton_3.setText(_translate("ShowGenre", "Back", None))
        self.pushButton_3.clicked.connect(self.close)
        self.pushButton_6.setText(_translate("ShowGenre", "Refresh", None))
        self.pushButton_6.clicked.connect(self.populateAllGenres)
