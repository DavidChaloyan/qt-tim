from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5.QtGui import QKeySequence
# from second import Ui_MainWindow
class Tool_bar:
    def __init__(self, object):
        self.tool_bar = self.toolBar = QtWidgets.QToolBar(object)
        self.tool_bar.setObjectName("toolBar")
        self.tool_bar.setStyleSheet("background-color: rgb(40, 40, 40);")
        runboton = self.tool_bar.addAction("Run")
        runboton.setShortcut(QKeySequence.Refresh)
        # runboton.triggered.connect(lambda: Ui_MainWindow.ran)
        
        # self.ran = Ui_MainWindow.s        # self.ran.ran()