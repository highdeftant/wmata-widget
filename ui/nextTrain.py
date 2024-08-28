#!/bin/env python3

# Pulls the next 1-4 trains departing from the station

def getcolor(trainline):

    colors = {
        "OR": '<img src=ui/traincolors/orange.png height="30">',
        "BL": '<img src=ui/traincolors/blue.png height="30">',
        "SV": '<img src=ui/traincolors/silver.png height="30">',
        "RD": '<img src=ui/traincolors/red.png height="30">',
        "YL": '<img src=ui/traincolors/yellow.png height="30">',
        "GR": '<img src=ui/traincolors/green.png height="30">'}

    colorcode = ''

    if trainline in colors.keys():
        colorcode = colors[trainline]

    return colorcode

def nextThree(trainfile):
    if 'Trains' in trainfile:
        result = '''
                    <html>
                        <body>
                            <table>
                                <tr style="background-color: #808080;">
                                    <th colspan="2"><b>Line</b></th>
                                    <th><b>Dest</b></th>
                                    <th><b>Min</b></th>
                                </tr>\n'''

        for train in trainfile['Trains'][:5]:
            if 'Line' in train and 'Destination' in train and 'Min' in train:
                result += '''
                                <tr style="background-color: #343434;">
                                    <td style='padding-right: 10px; padding-left: 10px;'>{}</td>
                                    <td style='padding-right: 10px; padding-left: 10px;'>{}</td>
                                    <td style='padding-right: 25px; padding-left: 10px;'>{}</td>
                                    <td style='padding-right: 10px; padding-left: 10px;'>{}</td>
                                </tr>\n'''.format(getcolor(train['Line']),
                                                  train['Line'],
                                                  train['Destination'],
                                                  train['Min'])
        result += '''       </table>
                        </body>
                    </html>'''

    return result

