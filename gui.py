import FreeSimpleGUI as sg
import functions

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo",key='todo')
add_button = sg.Button("Add")

window = sg.Window("My Simple Notes",
                   layout=[[label],[input_box,add_button]],
                   font=('Helvetica',14))

while True:
    event,values=window.read()
    match event:
        case 'Add':
            todos=functions.get_file()
            new_todo = values['todo'] +"\n"
            todos.append(new_todo)
            functions.write_file(todos)
        case sg.WIN_CLOSED:
            break


    print(event)
    print(values)
window.close()