from PyQt5 import QtCore, QtGui, QtWidgets


from PyQt5.QtWidgets import *
class Folder_place:

    def open_spaces(self, object):
        self.folder = QtWidgets.QDockWidget(object)
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
