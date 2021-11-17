# Create File Menu
from PyQt5 import QtWidgets
from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import *
from second import *


class File_menu:
    def menu_bar(self, menubar):
        ###########

        # self.menu_bar = QtWidgets.QMenuBar(main_window)
        # self.menu_bar.setObjectName("Menu Bar")
        self.file_menu = menubar.addMenu("&File")
        self.run_menu = menubar.addMenu("&Run")
        # new file
        new_file = self.file_menu.addAction("New File")
        new_file.triggered.connect(lambda: self.new_file())
        new_file.setShortcut(QKeySequence.New)
        # open file
        open_file = self.file_menu.addAction("Open File")
        open_file.triggered.connect(lambda: self.open_file(True))
        open_file.setShortcut(QKeySequence.Open)
        # open folder
        open_folder = self.file_menu.addAction("Open Folder")
        open_folder.triggered.connect(lambda: self.open_file(True))
        self.file_menu.addSeparator()
        # save
        save = self.file_menu.addAction("Save", lambda: self.click("ada"))
        save.triggered.connect(lambda: self.click(save.text()))
        save.setShortcut(QKeySequence.Save)
        # save as
        save_as = self.file_menu.addAction("Save AS", lambda: self.click("ada"))
        save_as.triggered.connect(lambda: self.click(save_as.text()))
        save_as.setShortcut(QKeySequence.SaveAs)
        # save all
        save_all = self.file_menu.addAction("Save All", lambda: self.click("ada"))
        save_all.triggered.connect(lambda: self.click(save_all.text()))
        self.file_menu.addSeparator()
        # close file
        close_file = self.file_menu.addAction("Close File", lambda: self.click("ada"))
        close_file.triggered.connect(lambda: self.click(close_file.text()))
        close_file.setShortcut(QKeySequence.Close)
        # close editor
        close_editor = self.file_menu.addAction("Close Editor", lambda: self.click("ada"))
        close_editor.triggered.connect(lambda: self.click(close_editor.text()))

    # my functions

    # new file
    def new_file(self):
        # fname = QFileDialog.n
        pass

    # open file
    def open_file(self, al):
        if al:
            fname = QFileDialog.accessibleName()[0]
            try:
                f = open(fname, "r")
                with f:
                    data = f.read()
                    print(data)
                    self.text_edit.appendPlainText(data)
            except FileNotFoundError:
                print("File not found")

    def save_file(self):
        fname = QFileDialog.saveFileContent()
