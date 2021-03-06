# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddAlbum.ui'
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

    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)

    @db_session
    def addAlbum(self):
        sBand = self.lineEditBand.text()
        isExistBand = select(c for c in mDB.Band if c.name is sBand)
        mDB.addAlbum(aTitle=self.lineEdit.text() , BandId=isExistBand.first().id)
        self.close()


    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(400, 251)
        self.verticalLayout_2 = QtGui.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.horizontalLayoutBand = QtGui.QHBoxLayout()
        self.horizontalLayoutBand.setObjectName(_fromUtf8("horizontalLayoutBand"))
        self.label = QtGui.QLabel(Form)
        self.labelBand = QtGui.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.labelBand.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.labelBand.setObjectName(_fromUtf8("labelBand"))
        self.horizontalLayout.addWidget(self.label)
        self.horizontalLayoutBand.addWidget(self.labelBand)
        self.lineEdit = QtGui.QLineEdit(Form)
        self.lineEditBand = QtGui.QLineEdit(Form)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEditBand.setObjectName(_fromUtf8("lineEditBand"))
        self.horizontalLayout.addWidget(self.lineEdit)
        self.horizontalLayoutBand.addWidget(self.lineEditBand)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout.addLayout(self.horizontalLayoutBand)
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.verticalLayout.addWidget(self.pushButton)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)


    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Add Album", None))
        self.label.setText(_translate("Form", "Title :", None))
        self.labelBand.setText(_translate("Form", "Band :", None))
        self.pushButton.setText(_translate("Form", "Submit", None))
        self.pushButton.clicked.connect(self.addAlbum)


    #TODO: Create addAlbum Function

