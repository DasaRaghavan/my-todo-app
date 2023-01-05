# todos = ['Clean', 'Cook', 'Prepare']
import os

FILENAME = "todos.txt"


def read_todos():
    """This function reads the todos from the todos.txt file. Returns an empty list if the file does not
    exist"""
    # filename = f"{filepath()}"
    try:
        with open(FILENAME, "r") as todos_file:
            todos_list: list[str] = todos_file.readlines()
        return todos_list
    except FileNotFoundError:
        # print("todos.txt will be created ...")
        # todos_file = open("todos.txt", "w")
        return []


def write_todos(fn_todos):
    """This function writes the todos to the todos.txt file. Returns None"""
    with open(FILENAME, "w") as todos_file:
        todos_file.writelines(fn_todos)
    return


if __name__ == "__main__":
    print(read_todos())
