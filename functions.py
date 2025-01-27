def get_file(filepath='text.txt'):
    """
    get input and store it to
    todos
    :param filepath:
    :return:
    """
    with open(filepath, 'r') as file:
        todos_new = file.readlines()
    return todos_new

def write_file (todos_arg, filepath='text.txt'):
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


# important
if __name__ == "__main__":

    print("hello from functions")