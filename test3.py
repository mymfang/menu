import PySimpleGUI as sg  

# Design pattern 1 - First window does not remain active  

layout = [[ sg.Text('Window1'),],  
          [sg.Input()],  
          #[sg.Text('', key='_OUTPUT_')],  
          [sg.Button('Launch 2')]]

win1 = sg.Window('Window1', layout)
win2_active = False

while True:
    event1, values1 = win1.read()
    if event1 is None:
        break
    
    if event1 == 'Launch 2' and not win2_active:
        win2_active = True
        win1.hide()
        layout2 = [
            [sg.Text('Window2')],
            [sg.Button('Exit')]
        ]

        win2 = sg.Window('Window2', layout2)
        while True:
            event2, values2 = win2.read()
            if event2 is None or event2 == 'Exit':
                win2.close()
                win2_acive = False
                win1.UnHide()
                break