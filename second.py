from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import *
from pyqtconsole.console import PythonConsole
import pyqtconsole.highlighter as hl
from subprocess import PIPE, run, check_output, Popen
import sys
import os


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Metax IDE")
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

        # proces = new Qprocess

        # Text editor
        self.textEdit = QtWidgets.QPlainTextEdit(MainWindow)
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setStyleSheet("background-color: rgb(38, 44, 60);color: rgb(240, 240, 240);")
        self.verticalLayout_2.addWidget(self.textEdit)

        # Menu bar
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 664, 22))
        self.menubar.setObjectName("menubar")

        # Creat File Menu
        fileMenu = self.menubar.addMenu("&File")
        newFile = fileMenu.addAction("New File")
        newFile.triggered.connect(lambda: self.newFile())
        newFile.setShortcut(QKeySequence.New)

        openFile = fileMenu.addAction("Open File")
        openFile.triggered.connect(lambda: self.OpenFile(True))
        openFile.setShortcut(QKeySequence.Open)

        openFolder = fileMenu.addAction("Open Folder")
        openFolder.triggered.connect(lambda: self.OpenFile(False))

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
        ran = runMenu.addAction("Run", lambda: self.ran(True))
        ran.setShortcut(QKeySequence.Refresh)
        debug = runMenu.addAction("Run Vim", lambda: self.debug(True))
        debug.setShortcut(Qt.CTRL + Qt.Key_D)
        runMenu.addSeparator()
        stopRun = runMenu.addAction("Stop", lambda: self.ran(False))
        stopRun.setShortcut(Qt.CTRL + Qt.SHIFT + Qt.Key_R)
        stopVim = runMenu.addAction("Stop Vim", lambda: self.debug(False))
        stopVim.setShortcut(Qt.CTRL + Qt.Key_D + Qt.SHIFT)

        # Create Terminal menu
        terminalMenu = self.menubar.addMenu("&Terminal")
        newTerm = terminalMenu.addAction("New Terminal")
        newTerm.triggered.connect(lambda: self.camand.clear())
        newTerm.setShortcut(Qt.CTRL + Qt.Key_T)
        clossTerm = terminalMenu.addAction("Close Terminal")
        clossTerm.triggered.connect(lambda: self.camand.close())
        clossTerm.setShortcut(Qt.CTRL + Qt.Key_T + Qt.SHIFT)

        # Make Help
        help = self.menubar.addAction("Help")
        help.triggered.connect(lambda: self.about())
        help.setShortcut(QKeySequence.HelpContents)

        #####
        MainWindow.setMenuBar(self.menubar)
        ##Status Bar
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        ## Toll BAr
        tolBar = self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        self.toolBar.setStyleSheet("background-color: rgb(40, 40, 40);")
        runboton = tolBar.addAction("Run")
        runboton.setShortcut(QKeySequence.Refresh)
        runboton.triggered.connect(lambda: self.ran(True))
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

        # camand Run
        self.camand = QtWidgets.QPlainTextEdit(self.dockWidgetContents_9)
        self.camand.setStyleSheet("background-color: rgb(30, 30, 30);color: rgb(255,255,255);separator")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.camand.sizePolicy().hasHeightForWidth())
        self.camand.setSizePolicy(sizePolicy)
        self.camand.setObjectName("camand")
        self.verticalLayout.addWidget(self.camand)
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
    #
    # def initUI(self):
    #     self.setWindowTitle(self.title)
    #     self.setGeometry(self.left, self.top, self.width, self.height)
    #
    #     self.model = QFileSystemModel()
    #     self.model.setRootPath('')
    #     self.tree = QTreeView()
    #     self.tree.setModel(self.model)
    #
    #     self.tree.setAnimated(False)
    #     self.tree.setIndentation(20)
    #     self.tree.setSortingEnabled(True)
    #
    #     self.tree.setWindowTitle("Dir View")
    #     self.tree.resize(640, 480)
    #
    #     windowLayout = QVBoxLayout()
    #     windowLayout.addWidget(self.tree)
    #     self.setLayout(windowLayout)
    #
    #     self.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))

    # @QtCore.pyqtSlot()
    def click(self, text):
        self.statusbar.showMessage(text, 2000)
        print("sjasvcsc")

    def debug(self, off):
        if off:
            command = self.camand.toPlainText()
            #result = run(command, stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True)
            
            result = Popen(command,stdout=PIPE ,shell=True)
            self.camand.clear()
            #self.camand.appendPlainText(str(result))
            print(result.stdout)
        else:
            pass
    def newFile(self):

        fname = QFileDialog.saveFileContent()

    def about(self):
        ms = QMessageBox()
        ms.setIcon(QMessageBox.Help)
        ms.setWindowTitle("About Author")
        ms.setText("This program  made in PONTEM LAB\nAddress: Shrjancik Tunel 7/1\nAuthors`\nTsolak Musikyan\n"
                   "Arsen Margaryan\nHayk Vardazaryan\nVahe Sedrakyan\nDavit Chaloyan\nXachik Hoxinyan")
        ms.exec_()
    def ran(self, off):
        if off:
            pass
        else:
            pass

    def OpenFile(self, al):
        if al:
            fname = QFileDialog.getOpenFileName()[0]

            try:
                f = open(fname, "r")
                with f:
                    data = f.read()
                    print(data)
                    self.textEdit.appendPlainText(data)
            except FileNotFoundError:
                print("File not found")

        # else:
        #     fname = QFileDialog.getExistingDirectory(self, "Folders", "./")


