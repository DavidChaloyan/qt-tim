from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import *
from pyqtconsole.console import PythonConsole
import pyqtconsole.highlighter as hl

import sys
import os



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(864, 598)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet("background-color: rgb(70, 70, 70);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")


        #proces = new Qprocess


        # Text editor
        self.textEdit = QtWidgets.QPlainTextEdit(MainWindow)
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setStyleSheet("background-color: rgb(38, 44, 60);")
        self.verticalLayout_2.addWidget(self.textEdit)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 864, 22))
        self.menubar.setObjectName("menubar")
        # Creat File Menu
        fileMenu = self.menubar.addMenu("&File")
        newFile = fileMenu.addAction("New File")
        newFile.triggered.connect(lambda: self.click(newFile.text()))
        newFile.setShortcut(QKeySequence.New)
        openFile = fileMenu.addAction("Open File")
        openFile.triggered.connect(lambda: self.click(openFile.text()))
        openFile.setShortcut(QKeySequence.Open)
        openFolder = fileMenu.addAction("Open Folder")
        openFolder.triggered.connect(lambda: self.click(openFolder.text()))

        fileMenu.addSeparator()
        save = fileMenu.addAction("Save", lambda: self.click("ada"))
        save.triggered.connect(lambda: self.click(save.text()))
        save.setShortcut(QKeySequence.Save)
        saveAs = fileMenu.addAction("Save AS", lambda: self.click("ada"))
        saveAs.triggered.connect(lambda: self.click(saveAs.text()))
        saveAs.setShortcut(QKeySequence.SaveAs)
        saveAll = fileMenu.addAction("Save All", lambda: self.click("ada"))
        saveAll.triggered.connect(lambda: self.click(saveAll.text()))
        fileMenu.addSeparator()
        closFile = fileMenu.addAction("Clos File", lambda: self.click("ada"))
        closFile.triggered.connect(lambda: self.click(closFile.text()))
        closFile.setShortcut(QKeySequence.Close)
        closeEditor = fileMenu.addAction("Clos Editor", lambda: self.click("ada"))
        closeEditor.triggered.connect(lambda: self.click(closeEditor.text()))

        # Creat Run menu
        runMenu = self.menubar.addMenu("&Run")
        runMenu.addAction("Run", lambda: self.click("dad"))
        runMenu.addAction("Debug", lambda: self.click("ada"))
        runMenu.addAction("Stop", lambda: self.click("ad"))
        runMenu.addAction("Stop Debug", lambda: self.click("das"))

        # Create Terminal menu
        terminalMenu = self.menubar.addMenu("&Terminal")
        newTerm = terminalMenu.addAction("New Terminal")
        newTerm.triggered.connect(lambda: self.click(newTerm.text()))
        splitTerm = terminalMenu.addAction("Split Terminal")
        splitTerm.triggered.connect(lambda: self.click(splitTerm.text()))


        # Make Help
        help = self.menubar.addAction("Help")
        help.triggered.connect(lambda: self.click(help.text()))
        help.setShortcut(QKeySequence.HelpContents)


        #####
        MainWindow.setMenuBar(self.menubar)
        ##Status Bar
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        ## Toll BAr
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        self.toolBar.setStyleSheet("background-color: rgb(40, 40, 40);")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        ## Console
        self.console = QtWidgets.QDockWidget(MainWindow)

        self.console.setStyleSheet("background-color: rgb(80, 89, 103);")

        self.console.setSizeIncrement(QtCore.QSize(0, 0))
        self.console.setStyleSheet("border:-5px")
        self.console.setInputMethodHints(QtCore.Qt.ImhNone)
        self.console.setObjectName("console")
        self.dockWidgetContents_9 = QtWidgets.QWidget()
        self.dockWidgetContents_9.setObjectName("dockWidgetContents_9")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.dockWidgetContents_9)
        self.verticalLayout.setObjectName("verticalLayout")
        #camand Run
        self.camand = PythonConsole(self.dockWidgetContents_9)
        self.camand.setStyleSheet("background-color: rgb(30, 30, 30);")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.camand.sizePolicy().hasHeightForWidth())
        self.camand.setSizePolicy(sizePolicy)
        self.camand.setObjectName("camand")
        self.verticalLayout.addWidget(self.camand)

        self.term = QtWidgets.QDockWidget(MainWindow)
        self.term.setStyleSheet("background-color: rgb(80, 89, 103);")
        #self.term.setGeometry(self.console.geometry())
        self.term.setSizeIncrement(QtCore.QSize(0, 0))
        self.term.setInputMethodHints(QtCore.Qt.ImhNone)
        self.term.setObjectName("term")
        self.dockWidgetContents_7 = QtWidgets.QWidget()
        self.dockWidgetContents_7.setObjectName("dockWidgetContents_7")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.dockWidgetContents_7)
        self.verticalLayout.setObjectName("verticalLayout")

        self.terminal = QtWidgets.QPlainTextEdit(self.dockWidgetContents_7)
        self.terminal.setStyleSheet("background-color: rgb(30, 30, 30);")

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.terminal.sizePolicy().hasHeightForWidth())
        self.terminal.setSizePolicy(sizePolicy)
        self.terminal.setObjectName("camand")
        self.verticalLayout.addWidget(self.terminal)
        self.term.setWidget(self.dockWidgetContents_7)
        buton = QAction("run")
        buton.setShortcut(QKeySequence.Refresh)
        buton.triggered.connect(lambda: self.click("apaaasas"))










        self.console.setWidget(self.dockWidgetContents_9)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(8), self.console)
        ##Folder place
        self.folder = QtWidgets.QDockWidget(MainWindow)
        self.folder.setObjectName("folder")
        self.folder.setStyleSheet("background-color: rgb(40, 40, 40);")
        self.dockWidgetContents_10 = QtWidgets.QWidget()
        self.dockWidgetContents_10.setObjectName("dockWidgetContents_10")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.dockWidgetContents_10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.treeView = QtWidgets.QTreeView(self.dockWidgetContents_10)
        self.treeView.setObjectName("treeView")
        self.horizontalLayout.addWidget(self.treeView)
        self.folder.setWidget(self.dockWidgetContents_10)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.folder)



        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))

    #@QtCore.pyqtSlot()
    def click(self, text):
        self.statusbar.showMessage(text, 2000)
        print("sjasvcsc")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()

    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
