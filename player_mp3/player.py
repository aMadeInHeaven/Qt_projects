from PyQt6 import QtWidgets, QtGui
from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput
import sys
from PyQt6.QtCore import QUrl
from design.playerUi import Ui_MainWindow


class player(Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.music_player = QMediaPlayer()
        self.setupUi(self)
        self.setup()
        self.list_of_music_names = []
        self.music_index = 0
        self.audioFormats = "*.mp3 *.wav"
        self.pause = False
        self.position = 0
        self.duration = 0

        self.audio_output = QAudioOutput()
        self.music_player.setAudioOutput(self.audio_output)
        self.audio_output.setVolume(50)

    def setup(self):
        self.play_btn.clicked.connect(self.play)
        self.next_btn.clicked.connect(self.next)
        self.prev_btn.clicked.connect(self.previous)
        self.music_list.doubleClicked.connect(self.change_song)
        self.add_song.clicked.connect(self.open)

        self.SongProgress_sldr.sliderMoved.connect(self.set_position)

        self.music_player.positionChanged.connect(self.position_changed)
        self.music_player.durationChanged.connect(self.duration_changed)
        self.music_player.playingChanged.connect(self.next_song_after_finish)

    def next_song_after_finish(self):
        if self.pause != True and self.SongProgress_sldr.value() == self.duration:
            if self.music_list.count()!=0:
                self.play_btn.setIcon(QtGui.QIcon("design/images/play.png"))
                music = self.music_list.takeItem(0).text()
                print(self.list_of_music_names[0])

                self.SongName_lbl.setText(music[:music.find(".")])

                self.music_player.setPosition(self.position)

                self.music_player.setSource(QUrl.fromLocalFile(self.list_of_music_names[self.music_index]))
                self.music_index += 1
                self.music_player.play()
            else:
                self.pause = True
                self.play_btn.setIcon(QtGui.QIcon("design/images/pause.png"))

    def set_position(self, position):
        self.music_player.setPosition(position)
        #print(self.music_player.position())

    def position_changed(self, position):
        #print(position)
        self.SongProgress_sldr.setValue(position)

    def duration_changed(self, duration):
        self.duration = duration
        self.SongProgress_sldr.setRange(0, duration)

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
        if self.music_list.count()>0:
            self.play_btn.setIcon(QtGui.QIcon("design/images/play.png"))
            music = self.music_list.takeItem(0).text()
            print(self.list_of_music_names[0])

            self.SongName_lbl.setText(music[:music.find(".")])

            self.music_player.setPosition(self.position)

            self.music_player.setSource(QUrl.fromLocalFile(self.list_of_music_names[self.music_index]))
            self.music_index += 1
            self.music_player.play()
            self.pause = False


    def change_song(self):
        pass

    def previous(self):
        pass

    def play(self):

        # print(f'self,pause {self.pause}')
        if self.music_player.isPlaying():
            self.pause = True
            self.music_player.pause()
            self.play_btn.setIcon(QtGui.QIcon("design/images/pause.png"))

        else:
            if self.pause:
                self.play_btn.setIcon(QtGui.QIcon("design/images/play.png"))
                self.pause = False
                self.music_player.play()

            elif self.music_list.count() > 0:
                self.play_btn.setIcon(QtGui.QIcon("design/images/play.png"))
                music = self.music_list.takeItem(0).text()
                print(self.list_of_music_names[0])

                self.SongName_lbl.setText(music[:music.find(".")])

                self.music_player.setPosition(self.position)

                self.music_player.setSource(QUrl.fromLocalFile(self.list_of_music_names[self.music_index]))
                self.music_index += 1
                self.music_player.play()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    window = player()
    window.show()

    app.exec()
