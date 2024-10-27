from PyQt6 import QtWidgets
import sys
from player_mp3.design.playerUi import Ui_MainWindow


class player(Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setup_btns()
        self.audioFormats = "*.mp3 *.wav *.ogg *.wma *.flac"

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
        pass

    def count_music_duration(self):
        pass


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    window = player()
    window.show()

    app.exec()
