import PySimpleGUI as simpleGui

import pyttsx3 as p
from gui import window

engine=p.init()
engine.say(' ')
engine.runAndWait

while True:
    event, values = window.read()
    if event == simpleGui.WINDOW_CLOSED:
        break
    
    


    '''After the user clicks the Speak button we check to see which radio button is selected, by default
    the male radio button is selected. Then if the user doesn't change the male radio button to female.
    Then we call the Speech Synthesizer class which is Synthesizer and pass all the arguments to make the engine
    perfome it's job'''
    if event == 'Speak':
        if values['-MALE-RB-']:
            voice="text "
        elif values['-FEMALE-RB-']:
            voice ="text "
        p.speak('text')

window.close()
