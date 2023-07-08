#!/bin/env python3

import backend
import sys
from PySide6 import QtCore, QtWidgets, QtGui, QtHelp

# ----Frontend Elements----

class Frontend(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        # Window
        self.setWindowTitle("WMATA Trains")
        self.button = QtWidgets.QPushButton("Update Times")
        self.text = QtWidgets.QLabel("Text to be updated",
                                    alignment=QtCore.Qt.AlignCenter)


    # ----Search Engine----        

        self.enginecore = QtHelp.QHelpEngineCore('../train_name_list.txt')
        self.searchengine = QtHelp.QHelpSearchEngine(self.enginecore)
        self.searchbar = QtHelp.QHelpSearchQueryWidget(self) 
        self.results = QtHelp.QHelpSearchResultWidget(self)
        self.layout = QtWidgets.QVBoxLayout(self)
        self.data = self.enginecore.setupData()

        self.layout.addWidget(self.searchbar)
        self.layout.addWidget(self.results)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)

    # ----Button Functions----

        self.button.clicked.connect(self.trainTime)
        self.searchbar.search.connect(self.search)
        self.searchbar.search.connect(self.trainTime)

    @QtCore.Slot()
    def search(self):
        station = self.searchbar.searchInput()
        num = self.searchengine.searchResultCount()
        self.searchengine.searchInput()
        self.searchengine.search(station)
        return

    @QtCore.Slot()
    def trainTime(self):
        code = backend.getStatCode(self.searchengine.searchInput())
        self.text.setText(backend.printTime(code))
     
if __name__ == "__main__":
    app = QtWidgets.QApplication()
    widget = Frontend()
    widget.resize(300, 180)
    widget.show()
    sys.exit(app.exec())

