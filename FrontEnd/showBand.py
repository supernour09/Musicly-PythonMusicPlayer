# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ShowBand.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from pony.orm import db_session
from FrontEnd import addBand,Player
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

class Ui_Band(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)


    def openAddBand(self):
        self.addBand = addBand.Ui_Form();
        self.addBand.show()

    @db_session
    def populateAllBands(self):
        self.listWidget.clear()
        self.bands = mDB.viewBands()
        for a in self.bands:
            self.listWidget.addItem('{:s}'.format(mDB.StringPrepere(a.name)))

    def play(self):
        self.player = Player.Ui_Form(self.bands[self.listWidget.currentRow()].songs)
        self.player.show()


    def setupUi(self, Band):
        Band.setObjectName(_fromUtf8("showBand"))
        Band.resize(670, 459)
        self.verticalLayout_2 = QtGui.QVBoxLayout(Band)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.listWidget = QtGui.QListWidget(Band)
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.verticalLayout.addWidget(self.listWidget)
        self.populateAllBands()
        self.listWidget.show()
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButton_5 = QtGui.QPushButton(Band)
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.horizontalLayout.addWidget(self.pushButton_5)
        self.pushButton = QtGui.QPushButton(Band)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_6 = QtGui.QPushButton(Band)
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.horizontalLayout.addWidget(self.pushButton_6)
        self.pushButton_3 = QtGui.QPushButton(Band)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Band)
        QtCore.QMetaObject.connectSlotsByName(Band)

    def retranslateUi(self, Band):
        Band.setWindowTitle(_translate("Band", "Bands", None))
        self.pushButton_5.setText(_translate("Band", "Add Band", None))
        self.pushButton_5.clicked.connect(self.openAddBand)
        self.pushButton.setText(_translate("Band", "Play", None))
        self.pushButton.clicked.connect(self.play)
        self.pushButton_3.setText(_translate("Band", "Back", None))
        self.pushButton_3.clicked.connect(self.close)
        self.pushButton_6.setText(_translate("ShowGenre", "Refresh", None))
        self.pushButton_6.clicked.connect(self.populateAllBands)
