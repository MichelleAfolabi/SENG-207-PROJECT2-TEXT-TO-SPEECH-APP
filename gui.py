import PySimpleGUI as simpleGui
#Difining the layout of the interface
layout = [[simpleGui.Input(key='-INPUT-TEXT-'), simpleGui.Button('Speak')],
          [simpleGui.Text('Select Voice Type'), simpleGui.Radio('Male', 'gender', True, key='-MALE-RB-'),
           simpleGui.Radio('Female', 'gender', key='-FEMALE-RB-')],
          ]

#Defining the frame of the window where everything will take place
window = simpleGui.Window('Text to Speech App', layout)


