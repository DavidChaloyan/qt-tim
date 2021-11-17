#from second import Ui_MainWindow
from PyQt5 import QtWidgets, QtCore
import terminal
import PyQt5
# from PyQt5 import QTermWidget
from pyqtconsole.console import PythonConsole 



class Console:
    def console_widget (self,main_window):
        self.console = QtWidgets.QDockWidget(main_window)
        self.console.setStyleSheet("background-color: rgb(80, 89, 103);")
        self.console.setSizeIncrement(QtCore.QSize(0, 0))
        self.console.setStyleSheet("border:-5px")
        self.console.setInputMethodHints(QtCore.Qt.ImhNone)
        self.console.setObjectName("console")
        self.dock_widget_contents_1 = QtWidgets.QWidget()
        self.dock_widget_contents_1.setObjectName("Dock Widgets")
        self.vertical_layout = QtWidgets.QVBoxLayout(self.dock_widget_contents_1)
        self.vertical_layout.setObjectName("vertical_Layout")
        # main_window.addDockWidgeets()
        # camand Run
        self.command = QtWidgets.QPlainTextEdit(self.dock_widget_contents_1)
        # self.command = PythonConsole(self.dock_widget_contents_1)
        # self.command = terminal.Terminal()#QtWidgets.QPlainTextEdit(self.dock_widget_contents_1)
        # self.command.write("ss")
        # self.command.dump()
        self.command.setStyleSheet("background-color: rgb(30, 30, 30);color: rgb(255,255,255);separator")
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.command.sizePolicy().hasHeightForWidth())
        self.command.setSizePolicy(size_policy)
        self.command.setObjectName("command")
        self.vertical_layout.addWidget(self.command)
        # self.command.eval_queued()
        self.console.setWidget(self.dock_widget_contents_1)

    def debug(self, off):
        if off:
            command = self.camand.toPlainText()
            #result = run(command, stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True)
            
            # result = Popen(command,stdout=PIPE ,shell=True)
            self.camand.clear()
            #self.camand.appendPlainText(str(result))
            # print(result.stdout)
        else:
            pass