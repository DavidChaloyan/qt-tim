from PyQt5 import QtGui, QtWidgets
# yyfrom PyQt5.QtWidgets import QApplication, QWidget, QPlainTextEdit, QVBoxLayout,QCompleter
import sys
import os


class Text_Edit():
    def __init__(self,main_window):
        super().__init__()
        self.text_edit = QtWidgets.QPlainTextEdit(main_window)
       
        self.text_edit.setObjectName("textEdit")
        self.text_edit.setStyleSheet("background-color: rgb(38, 44, 60);color: rgb(240, 240, 240);")
        

    def save (self):
        pass
