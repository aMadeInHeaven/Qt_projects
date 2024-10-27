from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMainWindow
import sys


class Window(object):
    def setup(self, MainWindow):
        super().__init__()

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)

        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(5, 0, 490, 570))
        self.textEdit.setObjectName("textEdit")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 26))
        self.menubar.setObjectName("menubar")

        self.File_menu = QtWidgets.QMenu(parent=self.menubar)
        self.File_menu.setObjectName("File_menu")
        MainWindow.setMenuBar(self.menubar)

        self.Save = QtGui.QAction()
        self.Save.setObjectName("Save")

        self.Save_as = QtGui.QAction()
        self.Save_as.setObjectName("Save_as")

        self.Open = QtGui.QAction()
        self.Open.setObjectName("Open")

        self.New = QtGui.QAction()
        self.New.setObjectName("New")

        self.File_menu.addAction(self.Open)
        self.File_menu.addSeparator()
        self.File_menu.addAction(self.New)
        self.File_menu.addSeparator()
        self.File_menu.addAction(self.Save)
        self.File_menu.addAction(self.Save_as)
        self.menubar.addAction(self.File_menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "New document"))
        self.File_menu.setTitle(_translate("MainWindow", "File"))
        self.Save.setText(_translate("MainWindow", "Save"))
        self.Save_as.setText(_translate("MainWindow", "Save as"))
        self.Open.setText(_translate("MainWindow", "Open"))
        self.New.setText(_translate("MainWindow", "New"))


'''Ниже для просмотра дизайна'''

if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Window()
    ui.setup(MainWindow)
    MainWindow.show()

    app.exec()
