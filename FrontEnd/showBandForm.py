# # -*- coding: utf-8 -*-
#
# # Form implementation generated from reading ui file 'Showband.ui'
# #
# # Created by: PyQt4 UI code generator 4.11.4
# #
# # WARNING! All changes made in this file will be lost!
#
# from PyQt4 import QtCore, QtGui
# from pony.orm import db_session
#
# try:
#     _fromUtf8 = QtCore.QString.fromUtf8
# except AttributeError:
#     def _fromUtf8(s):
#         return s
#
# try:
#     _encoding = QtGui.QApplication.UnicodeUTF8
#
#
#     def _translate(context, text, disambig):
#         return QtGui.QApplication.translate(context, text, disambig, _encoding)
# except AttributeError:
#     def _translate(context, text, disambig):
#         return QtGui.QApplication.translate(context, text, disambig)
#
#
# class Ui_Form(QtGui.QWidget):
#     def __init__(self, band):
#         self.band = band
#         QtGui.QWidget.__init__(self)
#         self.setupUi(self)
#         self.populateAllSongs()
#
#     def setupUi(self, Form):
#         Form.setObjectName(_fromUtf8("Form"))
#         Form.resize(440, 475)
#         self.verticalLayout_2 = QtGui.QVBoxLayout(Form)
#         self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
#         self.verticalLayout = QtGui.QVBoxLayout()
#         self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
#         self.horizontalLayout = QtGui.QHBoxLayout()
#         self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
#         self.label = QtGui.QLabel(Form)
#         font = QtGui.QFont()
#         font.setPointSize(12)
#         font.setBold(True)
#         font.setWeight(75)
#         self.label.setFont(font)
#         self.label.setObjectName(_fromUtf8("label"))
#         self.horizontalLayout.addWidget(self.label)
#         self.verticalLayout.addLayout(self.horizontalLayout)
#         self.horizontalLayout_2 = QtGui.QHBoxLayout()
#         self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
#         self.label_2 = QtGui.QLabel(Form)
#         font = QtGui.QFont()
#         font.setPointSize(12)
#         font.setBold(True)
#         font.setWeight(75)
#         self.label_2.setFont(font)
#         self.label_2.setObjectName(_fromUtf8("label_2"))
#         self.horizontalLayout_2.addWidget(self.label_2)
#         self.verticalLayout.addLayout(self.horizontalLayout_2)
#         self.listWidget = QtGui.QListWidget(Form)
#         self.listWidget.setObjectName(_fromUtf8("listWidget"))
#         self.verticalLayout.addWidget(self.listWidget)
#         self.pushButton = QtGui.QPushButton(Form)
#         self.pushButton.setObjectName(_fromUtf8("pushButton"))
#         self.verticalLayout.addWidget(self.pushButton)
#         self.verticalLayout_2.addLayout(self.verticalLayout)
#
#         self.retranslateUi(Form)
#         QtCore.QMetaObject.connectSlotsByName(Form)
#
#     @db_session
#     def show(self):
#         self.Songs = self.band.songs
#         print(len(self.Songs))
#         '''for p in self.bands:
#             self.listWidget.addItem(
#                 '{:s}{:s}'.format(mDB.StringPrepere(p.name), mDB.StringPrepere(':: Track ::' + str(len(p.songs)))))'''
#
#     def retranslateUi(self, Form):
#         Form.setWindowTitle(_translate("Form", "Show band", None))
#         self.label.setText(_translate("Form", "Name : " + self.band.name, None))
#         self.label_2.setText(_translate("Form", "Description : " + self.band.description, None))
#         self.pushButton.setText(_translate("Form", "Add Song", None))