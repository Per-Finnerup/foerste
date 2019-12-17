import PySimpleGUI as sg

sg.change_look_and_feel('Dark Blue 3')  # please make your creations colorful

layout = [  [sg.Text('Filename')],
            [sg.Input(key='minKey'), sg.FileBrowse()], 
            [sg.OK(), sg.Cancel()]] 

window = sg.Window('Get filename example', layout)

event, values = window.Read()
window.close()