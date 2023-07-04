FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """ this is a docstring ❤️ """
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


# print(help(get_todos()))


def write_todos(todos_arg, filename=FILEPATH):
    with open(filename, "w") as file:
        file.writelines(todos_arg)
