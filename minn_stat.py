#!/bin/env python3

import requests
import sys
import configparser 
from PySide6 import QtCore, QtWidgets, QtGui, QtHelp

# ---- API URL's, Links to files -----

alltrn_url = "https://api.wmata.com/StationPrediction.svc/json/GetPrediction/All"
minnave_url = "https://api.wmata.com/StationPrediction.svc/json/GetPrediction/D09"
farrwest_url = "https://api.wmata.com/StationPrediction.svc/json/GetPrediction/C03"
empt_url = "https://api.wmata.com/StationPrediction.svc/json/GetPrediction/{}"

config = configparser.ConfigParser()
config.read('config.ini')
wmatapi = config.get('API', 'key')
headers = {'api_key': wmatapi,}

repo = requests.get(minnave_url, headers)
getTrns = requests.get(alltrn_url, headers)
trnInfo = getTrns.json()

# ---- Backend Functions/Elements ----

def nextThree(trainfile): # Pulls the next 3 trains departing
    first_trn = trainfile['Trains'][0]
    sec_trn = trainfile['Trains'][1]
    thrd_trn = trainfile['Trains'][2]
    frth_trn = trainfile['Trains'][3]
    return ('Line' + ' ' + 'Dest' + ' ' + 'Min' + ' ' +
            first_trn['Line'] + ' ' + first_trn['Destination'] + ' ' + first_trn['Min'] + ' ' +
            sec_trn['Line'] + ' ' + sec_trn['Destination'] + ' ' + sec_trn['Min'] + ' ' +
            thrd_trn['Line'] + ' ' + thrd_trn['Destination'] + ' ' + thrd_trn['Min'])

def getStatCode(stationName):
    stationcode = []
    statname = trnInfo['Trains'] #list of dictionaries - trains 
    for trains in statname:
        if trains.get('LocationName') == stationName:
            stationcode.append(trains.get('LocationCode'))
            break
    return stationcode[0]

def printTime(stationcode):
    fill_url = empt_url.format(stationcode)
    statPull = requests.get(fill_url, headers)
    pulltime = statPull.json()
    return nextThree(pulltime)

def showTrns(): # Want this to show station info per station code in the parameter
    pass 

def getminnstat(): # Pulls current info for 'OR' line Minnesota Ave Station
    minn_sta = repo.json()
    first_trn = minn_sta['Trains'][0] #type <dict>
    sec_trn = minn_sta['Trains'][1]
    thrd_trn = minn_sta['Trains'][2]
    print("Dest" + " " + "Min")
    print(first_trn['Destination'] + ' ' + first_trn['Min'])
    print(sec_trn['Destination'] + ' ' + sec_trn['Min'])
    return thrd_trn['Destination'] + ' ' + thrd_trn['Min']

# ----Frontend Elements----

#class Frontend(QtWidgets.QWidget):

    def __init__(self):
        code = getStatCode(sys.argv[1])
        super().__init__()

        # Window
        self.setWindowTitle("WMATA Trains")
        self.button = QtWidgets.QPushButton("Update Times")
        self.text = QtWidgets.QLabel(printTime(code),
                                    alignment=QtCore.Qt.AlignCenter)

        
        self.searchbar = QtHelp.QHelpSearchQueryWidget() 
#        self.enginecore = QtHelp.QHelpEngineCore()
#        self.searchengine = QtHelp.QHelpSearchEngine()
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
        code = getStatCode(sys.argv[1])
        self.text.setText(printTime(code))
     


#if __name__ == "__main__":
    app = QtWidgets.QApplication()
    widget = Frontend()
    widget.resize(200, 150)
    widget.show()
    sys.exit(app.exec())


if len(sys.argv) > 1:
    code = getStatCode(sys.argv[1])
    print(printTime(code))
else:
    print(getminnstat())


#print(trnInfo)
