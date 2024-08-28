#!/bin/env python3

# Pulls the next 1-4 trains departing from the station

def getcolor():
    colors = {
        "OR": ,
        "BL": 20,
        "SV": 30,
        "RD": 40,
        "YL": 50,
        "GR": 60,
    }

def nextThree(trainfile):
    if 'Trains' in trainfile:
        result = '''
                    <html>
                        <body>
                            <table>
                                <tr style="background-color: #808080;">
                                    <th><b>Col</b></th>
                                    <th><b>Line</b></th>
                                    <th><b>Dest</b></th>
                                    <th><b>Min</b></th>
                                </tr>\n'''

        for train in trainfile['Trains'][:5]:
            if 'Line' in train and 'Destination' in train and 'Min' in train:
                result += '''
                                <tr style="background-color: #343434;">
                                    <td>{}</td>
                                    <td style='padding-right: 10px; padding-left: 10px;'>{}</td>
                                    <td style='padding-right: 25px; padding-left: 10px;'>{}</td>
                                    <td style='padding-right: 10px; padding-left: 10px;'>{}</td>
                                </tr>\n'''.format(" ",
                                                  train['Line'],
                                                  train['Destination'],
                                                  train['Min'])
        result += '''       </table>
                        </body>
                    </html>'''

    return result
