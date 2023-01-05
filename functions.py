# todos = ['Clean', 'Cook', 'Prepare']
import os

FILENAME = "todos.txt"


def filepath():
    """create a filepath of the todos file"""
    path = os.getenv("PWD")
    file_name = FILENAME
    file_path = f"{path}/{file_name}"
    return file_path


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


def show_todo(fn_todos):
    """This function shows the existing todos from the todos.txt file"""
    # n = 1
    # new_todos = [todo_item.strip('\n') for todo_item in fn_todos]
    for (index, fn_todo) in enumerate(fn_todos):
        fn_todo = fn_todo.strip('\n')
        print(f"{index + 1}. {fn_todo}")


def check_todos(fn_todos):
    """This function verifies if there is a todos.txt file"""
    if len(fn_todos) == 0:
        print("Todos does not exist. Do you want to create one? ")
        return
    else:
        print("Your todos are ...")
        show_todo(fn_todos)


def edit_todo(fn_todos, fn_user_action):
    """This function edits the todos"""
    item_number_to_edit = int(fn_user_action[5:])
    if item_number_to_edit <= len(fn_todos):
        item_number_to_edit = item_number_to_edit - 1
        fn_new_todo = input("Enter new todo: ") + "\n"
        fn_todos[item_number_to_edit] = fn_new_todo.capitalize()
    else:
        input_string = f"The item number {str(item_number_to_edit)} is not on the list. Do you want to add" \
                       f" it as item {str(len(fn_todos) + 1)} instead ? (Y/N) "
        response = input(input_string)
        match response.upper():
            case 'Y':
                print("The new todo will be added as item number", len(fn_todos) + 1)
                fn_new_todo = input("Enter new todo: ")
                fn_todos.append(fn_new_todo.capitalize())
            case 'N':
                print("Item WILL NOT be added")
            case _:
                print("invalid response. Item not added")
    return fn_todos


def complete_todo(fn_todos, fn_user_action):
    item_number_to_complete = fn_user_action[9:]
    if item_number_to_complete.isnumeric():
        item_number_to_complete = int(item_number_to_complete)
        if item_number_to_complete <= len(fn_todos):
            item_number_to_complete = item_number_to_complete - 1
            fn_todos.pop(item_number_to_complete)
            write_todos(fn_todos)
        else:
            show_todo(fn_todos)
            raise IndexError
    else:
        raise ValueError


if __name__ == "__main__":
    print(read_todos())
