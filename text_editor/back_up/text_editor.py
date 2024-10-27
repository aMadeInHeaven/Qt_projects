from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog
import sys
import os


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setObjectName("MainWindow")
        self.resize(500, 600)
        self.centralwidget = QtWidgets.QWidget()

        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(5, 0, 490, 570))
        self.textEdit.setObjectName("textEdit")

        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar()
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 26))
        self.menubar.setObjectName("menubar")

        self.File_menu = QtWidgets.QMenu(parent=self.menubar)
        self.File_menu.setObjectName("File_menu")
        self.setMenuBar(self.menubar)

        self.Save = QtGui.QAction()
        self.Save.setObjectName("Save")
        self.Save.triggered.connect(self.save)

        self.Save_as = QtGui.QAction()
        self.Save_as.setObjectName("Save_as")
        self.Save_as.triggered.connect(self.save_as)

        self.Open = QtGui.QAction()
        self.Open.setObjectName("Open")
        self.Open.triggered.connect(self.open)

        self.New = QtGui.QAction()
        self.New.setObjectName("New")
        self.New.triggered.connect(self.new)

        self.File_menu.addAction(self.Open)
        self.File_menu.addSeparator()
        self.File_menu.addAction(self.New)
        self.File_menu.addSeparator()
        self.File_menu.addAction(self.Save)
        self.File_menu.addAction(self.Save_as)
        self.menubar.addAction(self.File_menu.menuAction())

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        self.saved = False
        self.file_path = ""
        self.textEdit.textChanged.connect(self.change_saved)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.File_menu.setTitle(_translate("MainWindow", "File"))
        self.Save.setText(_translate("MainWindow", "Save"))
        self.Save_as.setText(_translate("MainWindow", "Save as"))
        self.Open.setText(_translate("MainWindow", "Open"))
        self.New.setText(_translate("MainWindow", "New"))

    def change_saved(self):
        self.saved = False

    def new(self):
        if not self.saved:

            wanna_save = QMessageBox()

            wanna_save.setWindowTitle("Do you want to save file?")
            wanna_save.setText("Wanna save the file?")

            wanna_save.setStandardButtons(
                QMessageBox.StandardButton.Cancel | QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)

            wanna_save.buttonClicked.connect(self.popup)

            wanna_save.exec()
        else:
            self.file_path = ""
            self.textEdit.clear()
            self.saved = False

    def popup(self, btn):
        text = btn.text()[1:]
        if text == "Yes":
            self.save()
            self.textEdit.clear()
            self.saved = False
        elif text == "No":
            self.textEdit.clear()
            self.saved = False

    def open(self):
        file_name = QFileDialog.getOpenFileName(self)[0]

        try:
            file = open(file_name, 'r')
            with file:
                self.textEdit.setText(file.read())
            self.saved = True
        except:
            print("some ship happened")

    def save(self):
        print(self.file_path)

        if not self.saved:

            try:
                print(1)
                file = open(self.file_path, 'w')

                text = self.textEdit.toPlainText()
                file.write(text)
                self.saved = True
            except:
                if self.file_path == "":
                    self.saved = True
                    self.save_as()
                else:
                    print("some ship happened")

    def save_as(self):
        file_name = QFileDialog.getSaveFileName(self)[0]

        try:
            print(1)
            file = open(file_name, 'w')
            self.file_path = file_name
            text = self.textEdit.toPlainText()
            file.write(text)
            self.saved = True
        except:
            print("some ship happened")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    app.exec()
