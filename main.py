import functions,time

now = time.strftime("%b %d,%Y %H:%M:%S")
print("Now Its",now)
while True:
    user_input = input("enter add, show,edit,complete")
    user_input = user_input.strip()

    if user_input.startswith('add'):
        todo = user_input[4:]
        todos = functions.get_file()

        todos.append(todo + '\n')

        functions.write_file(todos)
    elif 'show' in user_input:
        todos = functions.get_file()

        for index,item in enumerate(todos):
            print(f"{index + 1}-{item}")

    elif user_input.startswith('edit'):
        try:
            number = int(user_input[5:])
            user_input = user_input.strip()
            todos = functions.get_file()
            todo = input("enter todo")
            todos[number -1] = todo +'\n'

            functions.write_file(todos)
        except ValueError:
            print("your command is not valid")
            continue

    elif user_input.startswith('complete'):
        try:
            number = int(user_input[9:])

            todos = functions.get_file()

            todos.pop(number -1)

            functions.write_file(todos)
        except IndexError:
            print("there's no number fool!!")
            continue

