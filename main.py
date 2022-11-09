import PySimpleGUI as sg
import time
import ntpath
import re

sg.change_look_and_feel('Topanga')

background = sg.LOOK_AND_FEEL_TABLE['Topanga']['BACKGROUND']

delete_image_path = "icons/delete.png"
add_image_path = "icons/add.png"
sound_image_path = "icons/sound.png"
status_image_path = 'icons/status.png'
def open_window():
    layout = [[sg.Text("Choose your sound")],
              [sg.Input(key='-file-'), sg.FileBrowse()],
              [sg.Text("", key="-filename-")],
              [sg.OK(key='ok'), sg.Button("Close", key = "close")] 
              ]
    window2 = sg.Window("Sound", layout, modal=True)
    choice = None
    while True:
        event, values = window2.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == 'ok':
            path = values['-file-']
            basename = ntpath.basename(path)
            window2["-filename-"].Update(basename)
        if event == "close":
           window2.close()
saves = []
hours = ["%02d" % x for x in range(24)]
minutes = ["%02d" % x for x in range(60)]
def get_time():
    now = time.strftime("%H:%M:%S")
    window["-TIME-"].Update(now)

layout = [ [sg.Text("", key="-TIME-", text_color="cyan", font=("ds-digital", 20))],
           [sg.Combo(hours, key = '--hour--', size=(3,10), font='Arial 15'),
             sg.Combo(minutes, key = '--minute--', size=(3,10), font='Arial 15'),
            sg.Button(key="-plus-", image_filename=add_image_path, image_size=(50, 50), button_color = background,
           border_width=0),
           sg.Button(key="-minus-", image_filename=delete_image_path, image_size=(50, 50), button_color = background,
           border_width=0)],
            [sg.Listbox(saves, size=(17,10), select_mode=sg.SELECT_MODE_MULTIPLE, key='-LIST-', font='Arial 20')],
            [sg.Button(key="-sound-", image_filename=sound_image_path, image_size=(50, 50), button_color = background,
           border_width=0), sg.Button(key="-change-", image_filename=status_image_path, image_size=(50, 50),
            button_color = background, border_width=0)]]
           
            

    
window = sg.Window('Alarm', layout)
index = 0
while True:
    event, values = window.read(timeout=100) 
    if event == sg.WIN_CLOSED:
        break
    if event == '-plus-':
            index += 1
            hour_val = values["--hour--"]
            minute_val = values["--minute--"]
            selected=window['-LIST-'].get()
            saves.append(f"{index}.{hour_val}:{minute_val}:00")
            window['-LIST-'].Update(saves)
    if event == '-minus-':
            selected=window['-LIST-'].get()
            if selected != []:
               index -= 1
               saves.remove(selected[0])
               window['-LIST-'].Update(saves)
            else:
                pass   
    if event == '-sound-':
         open_window()
    if event == '-change-':
        selected = window['-LIST-'].get()
        num = saves.index(selected[0])
        if " Off" in selected[0]:
           changed = selected[0].replace(" Off", '')
           saves[num] = changed
           window['-LIST-'].Update(saves)
        else:
            saves[num] = selected[0] + " Off"
            window['-LIST-'].Update(saves)
    get_time()

window.close()
