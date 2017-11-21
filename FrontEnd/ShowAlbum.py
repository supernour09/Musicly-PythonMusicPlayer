# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ShowAlbums.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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


    def setupUi(self, ShowAlbum):
        ShowAlbum.setObjectName(_fromUtf8("ShowAlbum"))
        ShowAlbum.resize(680, 459)
        self.verticalLayout_2 = QtGui.QVBoxLayout(ShowAlbum)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.treeWidget = QtGui.QTreeWidget(ShowAlbum)
        self.treeWidget.setObjectName(_fromUtf8("treeWidget"))
        self.treeWidget.headerItem().setText(0, _fromUtf8("1"))
        self.verticalLayout.addWidget(self.treeWidget)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButton_5 = QtGui.QPushButton(ShowAlbum)
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.horizontalLayout.addWidget(self.pushButton_5)
        self.pushButton_2 = QtGui.QPushButton(ShowAlbum)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton = QtGui.QPushButton(ShowAlbum)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout.addWidget(self.pushButton)
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
        self.pushButton_2.setText(_translate("ShowAlbum", "ٍShow Album", None))
        self.pushButton.setText(_translate("ShowAlbum", "Play", None))
        self.pushButton_3.setText(_translate("ShowAlbum", "Back", None))
        self.pushButton_3.clicked.connect(self.close)
