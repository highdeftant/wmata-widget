#!/bin/env python3
import backend
import sys
from PySide6 import QtCore, QtQuick, QtWidgets, QtGui, QtHelp

# ----Frontend Elements----

class Frontend(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

    # ----  Window  ----
# These elements build the GUI Window

        self.setWindowTitle("WMATA Trains")
        self.button = QtWidgets.QPushButton("Update Times")
        self.text = QtWidgets.QLabel("Search Train Station",
                                    alignment=QtCore.Qt.AlignCenter)

    # ----  Search Engine   ----        
# Functions/Attributes for search engine

        self.enginecore = QtHelp.QHelpEngineCore('../train_name_list.txt')
        self.searchengine = QtHelp.QHelpSearchEngine(self.enginecore)
        self.searchbar = QtHelp.QHelpSearchQueryWidget(self)
        self.results = QtHelp.QHelpSearchResultWidget(self)
        self.layout = QtWidgets.QVBoxLayout(self)
        self.data = self.enginecore.setupData()

    # ----  Layout   ----
# Sets the layout for the windows

        self.layout.addWidget(self.searchbar)
        self.layout.addWidget(self.results)
        self.layout.addWidget(self.text)
    #    self.layout.addWidget(self.button)

    # ----  Button Functions    ----

        self.button.clicked.connect(self.trainTime)
        self.searchbar.search.connect(self.search)
        self.searchbar.search.connect(self.trainTime)

    #Uses textfile from backend to search for station names
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

    with open("ui/style.qss", "r") as f:
        _style = f.read()
        app.setStyleSheet(_style)

    widget = Frontend()
    widget.resize(340, 230)
    widget.show()
    sys.exit(app.exec())
