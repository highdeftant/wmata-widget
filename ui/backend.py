#!/bin/env python3

import requests
import sys
import configparser 
from PySide6 import QtCore, QtWidgets, QtGui, QtHelp

# ---- API URL's, Links to files -----

alltrn_url = "https://api.wmata.com/StationPrediction.svc/json/GetPrediction/All"
empt_url = "https://api.wmata.com/StationPrediction.svc/json/GetPrediction/{}"

config = configparser.ConfigParser()
config.read('config.ini')
wmatapi = config.get('API', 'key')
headers = {'api_key': wmatapi,}

getTrns = requests.get(alltrn_url, headers)
trnInfo = getTrns.json()

# ---- Backend Functions/Elements ----


# Pulls the next 1-4 trains departing from the station
def nextThree(trainfile):
    #todo:
    #this function should return one train, or 4 - completed 7/8
    if 'Trains' in trainfile:
        result = 'Line Dest Min\n'
        for train in trainfile['Trains'][:4]:
            if 'Line' in train and 'Destination' in train and 'Min' in train:
                result += '{} {} {}\n'.format(train['Line'], train['Destination'], train['Min'])
        return result


# This function grabs the station code from the station name used in the parameter
# todo: use either regex or standard string methods to match incorrect names for ease of use
def getStatCode(stationName):
    stationcode = []
    statname = trnInfo['Trains'] #list of dictionaries - trains 
    for trains in statname:
        if trains.get('LocationName') == stationName:
            stationcode.append(trains.get('LocationCode'))
            break
    return stationcode[0]

# Grabs every station name and writes it to a file for use on the frontend search engine
# todo: currently grabs multiple names of the same station when you only need one
def trainNames(): 
    statname = trnInfo['Trains']
    stations = [train['LocationName'] for train in statname]
    with open('train_name_list.txt', 'w') as statnames:
        for i in stations:
            statnames.write(i)
            statnames.write('\n')
    return 

# Can't really explain what this does cause I can't remember lol
def printTime(stationcode=''):
    fill_url = empt_url.format(stationcode)
    statPull = requests.get(fill_url, headers)
    pulltime = statPull.json()
    return nextThree(pulltime)


# Want this to show station info per station code in the parameter
def showTrns():
    pass 


#print(trnInfo)

