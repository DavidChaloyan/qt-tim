from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import *
# from pyqtconsole.console import PythonConsole
# import pyqtconsole.highlighter as hl
from subprocess import PIPE, Popen #STDOUT, run, check_output

# import file_menu
from consol_windget import Console
from folder_place import Folder_place
from pyt import Text_Edit
from file_menu import File_menu
from status_bar import Status_bar
from tool_bar import Tool_bar
from codeedit import *




class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Metax IDE")
        MainWindow.resize(864, 598)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(size_policy)
        MainWindow.setStyleSheet("background-color: rgb(70, 70, 70);")

        self.central_widget = QtWidgets.QWidget(MainWindow)
        self.central_widget.setObjectName("centralwidget")
        self.vertical_layout_2 = QtWidgets.QVBoxLayout(self.central_widget)
        self.vertical_layout_2.setObjectName("verticalLayout_2")

        # proces = new Qprocess

        # Text editor
        # self.text_edit = Text_Edit(MainWindow)
        self.ui = CodeEditor()
        # highlighter = PythonHighlighter(self.ui.document())
        self.vertical_layout_2.addWidget(self.ui)

        # # Menu bar
        MainWindow.setCentralWidget(self.central_widget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 664, 22))
        self.menubar.setObjectName("menubar")
        self.menubar.setVisible(True)
        menu_now = File_menu()
        menu_now.menu_bar(self.menubar)



        #####
        MainWindow.setMenuBar(self.menubar)
        # menubar = QtWidgets.QMenuBar(MainWindow)
        # # self.menubar = File_menu(MainWindow)
        # file = menubar.addMenu("File")
        # newfile = file.addAction("new file")
        # MainWindow.setMenuBar(menubar)
        # self.menubar.menu_bar.addMenu(file_mSenu)



        ####
        ##Status Bar
        # self.statusbar = Status_bar(MainWindow)
        # MainWindow.addStatusBar(self.statusbar.status_bar)

        ## Toll BAr
        self.toolBar = Tool_bar(MainWindow)

        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar.tool_bar)

        ## Console
        self.console = Console()
        self.console.console_widget(MainWindow)

        # camand Run
        self.camand = self.console.command
        # self.textEdit.setPlainText(str(self.camand.))

        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(8), self.console.console)

        ##Folder place
        self.folder = Folder_place()
        self.folder.open_spaces(MainWindow)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.folder.folder)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Metax IDE", "Metax IDE"))
        self.menubar.setWindowTitle(_translate("MainWindow", "menubar"))
        # self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))

    # @QtCore.pyqtSlot()
    def click(self, text):
        # self.statusbar.showMessage(text, 2000)
        print("sjasvcsc")

    def ran(self):
        codes = self.text_edit.text_edit.toPlainText
        with open('runfile.py', 'w') as f:
            f.write(codes)
        self.camand.clear()
        result = Popen("python3" + "runfile.py", stdout=PIPE, shell=True)
        self.camand.setPlainText(result.stdout)

    def debug(self, off):
        if off:
            command = self.camand.toPlainText()
            # result = run(command, stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True)

            result = Popen(command, stdout=PIPE, shell=True)
            self.camand.clear()
            # self.camand.appendPlainText(str(result))
            print(result.stdout)
        else:
            pass

    def newFile(self):

        fname = QFileDialog.saveFileContent()

    def about(self):
        ms = QMessageBox()
        # ms.setIcon(QMessageBox)
        ms.setWindowTitle("About Author")
        ms.setText("This program  made in PONTEM LAB\nAddress: Shrjancik Tunel 7/1\nAuthors`\nTsolak Musikyan\n"
                   "Arsen Margaryan\nHayk Vardazaryan\nVahe Sedrakyan\nDavit Chaloyan\nXachik Hoxinyan")
        ms.exec_()

    # def ran(self, off):
    # if off:
    #     pass
    # else:
    #     pass

    # def OpenFile(self, al):
    #     if al:
    #         fname = QFileDialog.getOpenFileName()[0]
    #
    #         try:
    #             f = open(fname, "r")
    #             with f:
    #                 data = f.read()
    #                 print(data)
    #                 self.text_edit.text_edit.appendPlainText(data)
    #         except FileNotFoundError:
    #             print("File not found")

        # else:
        #     fname = QFileDialog.getExistingDirectory(self, "Folders", "./")
