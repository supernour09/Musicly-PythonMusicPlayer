# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ShowArtisit.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from FrontEnd import addBand

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


    def openAddBand(self):
        self.addBand= addBand.Ui_Form();
        self.addBand.show()

    def setupUi(self, Artisit):
        Artisit.setObjectName(_fromUtf8("Artisit"))
        Artisit.resize(670, 459)
        self.verticalLayout_2 = QtGui.QVBoxLayout(Artisit)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.treeWidget = QtGui.QTreeWidget(Artisit)
        self.treeWidget.setObjectName(_fromUtf8("treeWidget"))
        self.treeWidget.headerItem().setText(0, _fromUtf8("1"))
        self.verticalLayout.addWidget(self.treeWidget)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButton_5 = QtGui.QPushButton(Artisit)
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.horizontalLayout.addWidget(self.pushButton_5)
        self.pushButton_2 = QtGui.QPushButton(Artisit)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton = QtGui.QPushButton(Artisit)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_3 = QtGui.QPushButton(Artisit)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Artisit)
        QtCore.QMetaObject.connectSlotsByName(Artisit)

    def retranslateUi(self, Artisit):
        Artisit.setWindowTitle(_translate("Artisit", "Bands", None))
        self.pushButton_5.setText(_translate("Artisit", "Add Band", None))
        self.pushButton_5.clicked.connect(self.openAddBand)
        self.pushButton_2.setText(_translate("Artisit", "ٍShow Band", None))
        self.pushButton.setText(_translate("Artisit", "Play", None))
        self.pushButton_3.setText(_translate("Artisit", "Back", None))
        self.pushButton_3.clicked.connect(self.close)
