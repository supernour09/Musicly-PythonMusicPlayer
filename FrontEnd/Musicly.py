# -*- coding: utf-8 -*-

import sys

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!
from FrontEnd import AddSong,ShowAlbum, ShowGenre, playLists
from PyQt4 import QtCore, QtGui
from FrontEnd import ShowArtisit


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

    def openPlayList(self):
        self.playList = playLists.Ui_PlayList();
        self.playList.show()

    def openAlbum(self):
        self.album = ShowAlbum.Ui_ShowAlbum()
        self.album.show()

    def openArtisit(self):
        self.artisit = ShowArtisit.Ui_Artisit()
        self.artisit.show()

    def openGenre(self):
        self.genre = ShowGenre.Ui_ShowGenre()
        self.genre.show()

    def openAddSong(self):
        self.addSong = AddSong.Ui_AddSong()
        self.addSong.show()

    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(623, 441)
        self.verticalLayout_2 = QtGui.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButton_5 = QtGui.QPushButton(Form)
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.horizontalLayout.addWidget(self.pushButton_5)
        self.pushButton_2 = QtGui.QPushButton(Form)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_3 = QtGui.QPushButton(Form)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton_4 = QtGui.QPushButton(Form)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Musicly", None))
        self.label.setText(_translate("Form", "<html><head/><body><p>Welcome to musicly </p><p> made By Nour &amp;&amp; Mazen</p></body></html>", None))
        self.pushButton_5.setText(_translate("Form", "Show Playlist", None))
        self.pushButton_5.clicked.connect(self.openPlayList)
        self.pushButton_2.setText(_translate("Form", "ٍShow Albums", None))
        self.pushButton_2.clicked.connect(self.openAlbum)
        self.pushButton.setText(_translate("Form", "Show Bands ", None))
        self.pushButton.clicked.connect(self.openArtisit)
        self.pushButton_3.setText(_translate("Form", "Show Genre", None))
        self.pushButton_3.clicked.connect(self.openGenre)
        self.pushButton_4.setText(_translate("Form", "Add Song", None))
        self.pushButton_4.clicked.connect(self.openAddSong)


'''
@db_session
def test():
    select(p for p in MusiclyDB.db.Person).show()

@db_session
def pop():
    person = MusiclyDB.db.Person(name='John')
    MusiclyDB.db.commit()

'''


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = Ui_Form()
    ex.show()
    sys.exit(app.exec())
