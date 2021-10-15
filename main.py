import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from first import Ui_MainWindow1
from second import Ui_MainWindow

app = QtWidgets.QApplication(sys.argv)

first = QtWidgets.QMainWindow()
ui = Ui_MainWindow1()
ui.setupUi(first)
first.show()


def openSecond():
    global second
    second = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(second)
    first.close()
    second.show()


def openfile():
    global MainWindow
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    first.close()
    MainWindow.show()
    ui.OpenFile(True)


ui.newProject.clicked.connect(openSecond)
ui.openProject.clicked.connect(openfile)
sys.exit(app.exec_())
