# print("Enter a todo :")
# user_text = input("Enter a todo :")
# print(user_text)
# user_prompt = "Enter the todo :"
# todo1 = input(user_prompt)
# todo2 = input(user_prompt)
# todos = [todo1,todo2]
# print(todos)


# todos = []
from functions import get_todos,write_todos
# import functions
import time
now=time.strftime("%b %d, %Y %H:%M:%S")
print("It is",now)
while True:
    user_action = input("Type add,show,edit,complete or exit : ")
    user_action = user_action.strip()

    # if "add" in user_action:
    if user_action.startswith("add"):
        # todo = input("Enter the todo : ") + "\n"
        # file = open("todos.txt", "r")
        # todos = file.readlines()
        todo = user_action[4:]
        todos = get_todos()
        todos.append(todo + "\n")

        write_todos(todos)
        # functions.write_todos(todos)

        # file = open("todos.txt", "w")
        # file.writelines(todos)
    elif user_action.startswith("show"):
        # file = open("todos.txt", "r")
        # todos = file.readlines()
        # file.close()
        todos = get_todos()
        print(todos)
        # new_todos=[]
        # for item in todos:
        #     new_item = item.strip("\n")
        #     new_todos.append(new_item)
        # #  list comprehension
        #  list is created on the fly
        # new_todos=[item.strip("\n") for item in todos]
        for index, item in enumerate(todos):
            item = item.strip("\n")
            item = item.title()
            row = f"{index + 1}){item}"
            print(row)
    elif user_action.startswith("exit"):
        print("Bye ❤️")
        break
    elif user_action.startswith("edit"):
        try:
            # number = int(input("Enter the  number of the todo to edit : "))
            number = int(user_action[5:])
            number = number - 1
            todos = get_todos()
            new_todo = input("Enter the new todo : ")
            todos[number] = new_todo + "\n"
            # with open("todos.txt", "w") as file:
            #     file.writelines(todos)
            write_todos(todos)
        except ValueError:
            print("This is an invalid command 😢")
            continue
            # todo_number = todos[number]
            # print(todo_number)
    elif user_action.startswith("complete"):
        try:
            # number = int(input("Number of the todo which has been completed : "))
            number = int(user_action[9:])
            todos = get_todos()
            index = number - 1
            todo_to_remove = todos[index].strip("\n")
            todos.pop(index)
            write_todos(todos)
            # with open("todos.txt", "w") as file:
            #     file.writelines(todos)
            message = f"Todo {todo_to_remove} has been removed...."
            print(message)
        except IndexError:
            print("There is no item in the list with that number.")
            continue
    else:
        print("Hey, this is an unknown command")
