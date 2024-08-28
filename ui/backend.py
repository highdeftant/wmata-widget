#!/bin/env python3

import requests, sys, configparser, os
from PySide6 import QtCore, QtWidgets, QtGui, QtHelp

# ----  API URL's, Links to files    -----

alltrn_url = "https://api.wmata.com/StationPrediction.svc/json/GetPrediction/All"
empt_url = "https://api.wmata.com/StationPrediction.svc/json/GetPrediction/{}"


# ----  Backend Functions/Elements  ----

config = configparser.ConfigParser()
config.read('config.ini')
wmatapi = config.get('API', 'key')
headers = {'api_key': wmatapi,}
getTrns = requests.get(alltrn_url, headers)
trnInfo = getTrns.json()

# Pulls the next 1-4 trains departing from the station
def nextThree(trainfile):
    if 'Trains' in trainfile:
        result = '''
                    <html>
                        <body>
                            <table>
                            <tr>
                                <th><b>Line</b></th>
                                <th><b>Dest</b></th>
                                <th><b>Min</b></th>
                            </tr>\n'''

        for train in trainfile['Trains'][:4]:
            if 'Line' in train and 'Destination' in train and 'Min' in train:
                result += '''
                        <tr>
                            <td>{}</td>
                            <td>{}</td>
                            <td>{}</td>
                        </tr>'''.format(train['Line'],
                                        train['Destination'],
                                        train['Min'])
    result += '''</table>
                </body>
                </html>'''

    return result

# This function grabs the station code from the station name used in the parameter
# todo: use either regex or standard string methods to match incorrect names for ease of use
def getStatCode(stationName):
    stationcode = []
    statname = trnInfo['Trains'] #list of dictionaries - trains 
    for trains in statname:
        if trains.get('LocationName').lower() == stationName or trains.get('LocationName') == stationName:
            stationcode.append(trains.get('LocationCode'))
            break
    return stationcode[0]

# Grabs every station name and writes it to a file -
# for use on the frontend search engine

def trainNames():
    statname = trnInfo['Trains']
    stations = [train['LocationName'] for train in statname]

    if getTrns.status_code != 200:
        if os.path.exists('train_name_list.txt'):
            with open('train_name_list.txt', 'r') as statnames:
                statnames.read().splitlines()
        else:
            with open('train_name_list.txt', 'w') as statnames:
                stationlist = []
                for name in stations:
                    if name not in stationlist:
                        statnames.write(name)
                        statnames.write('\n')
                        stationlist.append(name)
    return

# Takes the empty URL and fills it to pull full list of trains
def printTime(stationcode=''):
    fill_url = empt_url.format(stationcode)
    statPull = requests.get(fill_url, headers)
    pulltime = statPull.json()
    return nextThree(pulltime)

# Want this to show station info per station code in the parameter
def showTrns():
    pass

if __name__ == "__main__":
    trainNames()
