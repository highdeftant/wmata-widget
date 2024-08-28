#!/bin/env python3

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

        for train in trainfile['Trains'][:5]:
            if 'Line' in train and 'Destination' in train and 'Min' in train:
                result += '''
                                <tr>
                                    <td>{}</td>
                                    <td>{}</td>
                                    <td>{}</td>
                                </tr>\n'''.format(train['Line'],
                                                  train['Destination'],
                                                  train['Min'])
        result += '''       </table>
                        </body>
                    </html>'''

    return result
