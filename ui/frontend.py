#!/bin/env python3

import backend
import sys
from PySide6 import QtCore, QtWidgets, QtGui, QtHelp

# ----Frontend Elements----

class Frontend(QtWidgets.QWidget):

    def __init__(self):
        code = backend.getStatCode(sys.argv[1])
        super().__init__()

        # Window
        self.setWindowTitle("WMATA Trains")
        self.button = QtWidgets.QPushButton("Update Times")
        self.text = QtWidgets.QLabel(backend.printTime(code),
                                    alignment=QtCore.Qt.AlignCenter)

        
        self.searchbar = QtHelp.QHelpSearchQueryWidget() 
       # self.enginecore = QtHelp.QHelpEngineCore()
       # self.searchengine = QtHelp.QHelpSearchEngine()
        self.layout = QtWidgets.QVBoxLayout(self)


        self.layout.addWidget(self.searchbar)
        #self.layout.addWidget(QtHelp.QHelpSearchResult())
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)
        self.button.clicked.connect(self.trainTime)


    @QtCore.Slot()
    def something(self):
        pass


    @QtCore.Slot()
    def trainTime(self):
        code = backend.getStatCode(sys.argv[1])
        self.text.setText(backend.printTime(code))
     

if __name__ == "__main__":
    app = QtWidgets.QApplication()
    widget = Frontend()
    widget.resize(200, 150)
    widget.show()
    sys.exit(app.exec())


#if len(sys.argv) > 1:
#    code = getStatCode(sys.argv[1])
#    print(printTime(code))
#else:
#    print(getminnstat())


#print(trnInfo)
