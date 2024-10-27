from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog
from text_editor.design.text_editor_settinffile import Window
import sys


class Main_window(QMainWindow, Window):
    def __init__(self):
        super().__init__()
        self.setup(self)
        self.setup1()
        self.saved = False
        self.file_path = ""

    def setup1(self):
        self.Save.triggered.connect(self.save)
        self.Save_as.triggered.connect(self.save_as)
        self.Open.triggered.connect(self.open)
        self.New.triggered.connect(self.new)

        self.textEdit.textChanged.connect(self.change_saved)

    def change_saved(self):
        self.saved = False

    def new(self):
        if not self.saved:

            wanna_save = QMessageBox()

            wanna_save.setWindowTitle("Do you want to save file?")
            wanna_save.setText("Wanna save the file?")

            wanna_save.setStandardButtons(
                QMessageBox.StandardButton.Cancel | QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)

            wanna_save.exec()
            result = wanna_save.standardButton(wanna_save.clickedButton())
            if result == QMessageBox.StandardButton.Yes:
                self.save()
                self.clear_document()
            elif result == QMessageBox.StandardButton.No:
                self.clear_document()

        else:
            self.clear_document()

    def clear_document(self):

        self.textEdit.clear()
        self.file_path = ""
        self.setWindowTitle("New document")
        self.saved = False

    def open(self):
        file_name = QFileDialog.getOpenFileName(self, caption="Choose txt file", filter="Text files (*.txt)")[0]
        print(file_name)
        try:
            file = open(file_name, 'r')
            with file:
                self.textEdit.setText(file.read())
            self.saved = True
            self.setWindowTitle(file_name.split("/")[-1])
            self.file_path = file_name
        except FileNotFoundError:
            print("error")
        print(self.file_path)

    def save(self):
        print(self.file_path)
        if self.file_path == "":
            self.save_as()
        else:
            if not self.saved:
                if self.file_path == "":
                    self.saved = True
                    self.save_as()
                else:
                    try:
                        print(1)
                        file = open(self.file_path, 'w')

                        text = self.textEdit.toPlainText()
                        file.write(text)
                        self.saved = True
                    except FileNotFoundError:

                        print("file not found")

    def save_as(self):
        file_name = QFileDialog.getSaveFileName(self, filter="Text files (*.txt)")[0]

        try:
            file = open(file_name, 'w')
            self.file_path = file_name
            text = self.textEdit.toPlainText()
            file.write(text)
            self.setWindowTitle(file_name.split("/")[-1])
            self.saved = True
        except FileNotFoundError:
            print("file don't chosen")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Main_window()
    window.show()

    app.exec()
