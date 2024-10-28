from PyQt6 import QtWidgets, QtGui
from pygame import mixer
import sys
from player_mp3.design.playerUi import Ui_MainWindow


class player(Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        mixer.init()
        self.setupUi(self)
        self.setup_btns()
        self.list_of_music_names = []
        self.audioFormats = "*.mp3 *.wav *.ogg *.wma *.flac"
        self.pause = False

    def setup_btns(self):
        #self.SongProgress_sldr.connect(self.count_music_duration)
        self.play_btn.clicked.connect(self.play)
        self.next_btn.clicked.connect(self.next)
        self.prev_btn.clicked.connect(self.previous)
        self.music_list.doubleClicked.connect(self.change_song)
        self.add_song.clicked.connect(self.open)

    def open(self):
        # file_name = QFileDialog.getOpenFileName(self)[0]
        files = QtWidgets.QFileDialog.getOpenFileNames(self, caption="Choose music file", filter=self.audioFormats)
        files = list(files)[:-1]

        files = files[0]

        try:
            for file in files:
                self.list_of_music_names += [file]
                self.music_list.addItem(file.split("/")[-1])
                print(file)

        except:
            print("some shit happened")

    def next(self):
        pass

    def change_song(self):
        pass

    def previous(self):
        pass

    def play(self):
        if mixer.music.get_busy():
            self.play_btn.setIcon(QtGui.QIcon("design/images/pause.png"))
            mixer.music.pause()
            self.pause = True
        else:
            if self.pause:
                self.play_btn.setIcon(QtGui.QIcon("design/images/play.png"))
                mixer.music.unpause()
                self.pause = False
            else:
                if self.music_list.count() > 0:
                    self.play_btn.setIcon(QtGui.QIcon("design/images/play.png"))
                    music = self.music_list.takeItem(0).text()
                    print(music)
                    self.SongName_lbl.setText(music[:music.find(".")])
                    mixer.music.load(self.list_of_music_names[0])
                    mixer.music.play()
                    self.list_of_music_names.pop(0)

    def count_music_duration(self):
        pass


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    window = player()
    window.show()

    app.exec()
