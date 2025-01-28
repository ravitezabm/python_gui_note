import FreeSimpleGUI as sg
import functions


label = sg.Text("My to-do")
input_box = sg.InputText(tooltip="Enter To-do",key='todo')
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_file(),key='todos',
                      enable_events=True,size=[45,20])
edit_button = sg.Button('Edit')
complete_button = sg.Button('Complete')
exit_button = sg.Button('Exit')


window = sg.Window('Daily Notes',
                   layout=[[label],[input_box,add_button],
                           [list_box,edit_button,complete_button],
                           [exit_button]],
                   font=('Helvetica',14))

while True:
    event,values = window.read()
    print(event)
    print(values)
    match event:
        case 'Add':
            todos = functions.get_file()
            todo_new = values['todo'] + "\n"
            todos.append(todo_new)
            functions.write_file(todos)
            window['todos'].update(todos)
        case 'Edit':
            todo_to_edit = values['todos'][0]
            new_todo = values['todo']
            todos = functions.get_file()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_file(todos)
            window['todos'].update(todos)
        case 'todos':
            window['todo'].update(value=values['todos'][0])

        case 'Complete':
            todo_to_complete = values['todos'][0]
            todos = functions.get_file()
            todos.remove(todo_to_complete)
            functions.write_file(todos)
            window['todos'].update(todos)
            window['todo'].update('')

        case 'Exit':
            break

        case sg.WIN_CLOSED:
            break

window.close()