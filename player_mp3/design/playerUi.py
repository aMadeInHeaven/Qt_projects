from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(700, 250)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.SongName_lbl = QtWidgets.QLabel(parent=self.centralwidget)
        self.SongName_lbl.setGeometry(QtCore.QRect(0, 10, 320, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.SongName_lbl.setFont(font)
        self.SongName_lbl.setStyleSheet("background-color: rgb(61, 61, 61);\n"
                                        "color: rgb(28, 255, 25);")
        self.SongName_lbl.setText("")
        self.SongName_lbl.setObjectName("SongName_lbl")
        self.SongName_lbl.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        self.SongProgress_sldr = QtWidgets.QSlider(parent=self.centralwidget)
        self.SongProgress_sldr.setGeometry(QtCore.QRect(0, 75, 320, 30))
        self.SongProgress_sldr.setStyleSheet("border-color: rgb(255, 0, 0);\n"
                                             "background-color: rgb(70, 70, 70);")
        self.SongProgress_sldr.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.SongProgress_sldr.setObjectName("SongProgress_sldr")

        self.prev_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.prev_btn.setGeometry(QtCore.QRect(10, 120, 70, 70))
        self.prev_btn.setStyleSheet("background-color: rgb(214, 214, 214);")
        self.prev_btn.setText("")
        self.prev_btn.setObjectName("prev_btn")
        self.prev_btn.setIcon(QtGui.QIcon("design/images/previous.png"))
        self.prev_btn.setIconSize(QtCore.QSize(65, 65))

        self.add_song = QtWidgets.QPushButton(parent=self.centralwidget)
        self.add_song.setGeometry(QtCore.QRect(2, 218, 95, 30))
        self.add_song.setStyleSheet("background-color: rgb(214, 214, 214);")
        self.add_song.setText("Add song")
        self.add_song.setObjectName("add_song")

        self.play_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.play_btn.setGeometry(QtCore.QRect(125, 120, 70, 70))
        self.play_btn.setStyleSheet("background-color: rgb(214, 214, 214);")
        self.play_btn.setText("")
        self.play_btn.setObjectName("play_btn")
        self.play_btn.setIcon(QtGui.QIcon("design/images/pause.png"))
        self.play_btn.setIconSize(QtCore.QSize(65, 65))

        self.next_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.next_btn.setGeometry(QtCore.QRect(240, 120, 70, 70))
        self.next_btn.setStyleSheet("background-color: rgb(214, 214, 214);")
        self.next_btn.setText("")
        self.next_btn.setObjectName("next_btn")
        self.next_btn.setIcon(QtGui.QIcon("design/images/next.png"))
        self.next_btn.setIconSize(QtCore.QSize(65, 65))

        self.music_list = QtWidgets.QListWidget(parent=self.centralwidget)
        self.music_list.setGeometry(QtCore.QRect(368, 2, 330, 246))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.music_list.setFont(font)
        self.music_list.setStyleSheet("color: rgb(210, 255, 125);\n"
                                      "border-color: rgb(81, 255, 6);")
        self.music_list.setObjectName("music_list")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
