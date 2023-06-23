import QtQuick 2.0
import QtQuick.Controls 2.10



ApplicationWindow {
    visible: true
    width: 540
    height: 480
    title: "WMATA KDE-Widget"

    Rectangle {
        color: "darkorange"
        width: 800
        height: 200
    }


    Column {
        anchors.centerIn: parent
        spacing: 10


    Text {
        id: infoText
        text: "Text will be updated" 
        font.pointSize: 14

    }


        Button {
            text: "Click me!"
            onClicked: {
                trainTime()
                // console.log("Button clicked!")
                // Call a function or perform an action here
            }
        }
    }
}

