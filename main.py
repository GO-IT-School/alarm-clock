import PySimpleGUI as sg
import time


sg.theme('Topanga')  
saves = []
def get_time():
    now = time.strftime("%H:%M:%S")
    window["-TIME-"].Update(now)

layout = [ [sg.Text("", key="-TIME-", text_color="cyan", font=("ds-digital", 20))], 
           [sg.InputText(key = '--hour--', size=(7,10), font='Arial 10'),
             sg.InputText(key = '--minute--', size=(7,10), font='Arial 10'),
            sg.Button('Save', size=(8,1), key="-plus-"),
           sg.Button("Delete", size=(8,1), key="-minus-")],
            [sg.Listbox(saves, size=(17,10), select_mode=sg.SELECT_MODE_MULTIPLE, key='-LIST-', font='Arial 20')]]
            

    
window = sg.Window('Alarm', layout)

while True:
    event, values = window.read(timeout=100) 
    if event == sg.WIN_CLOSED:
        break
    if event == '-plus-':
            hour_val = values["--hour--"]
            minute_val = values["--minute--"]
            selected=window['-LIST-'].get()
            saves.append(f"{hour_val}:{minute_val}:00")
            window['-LIST-'].Update(saves)
    if event == '-minus-':
            selected=window['-LIST-'].get()
            saves.remove(selected[0])
            window['-LIST-'].Update(saves)
    get_time()

window.close()
