import streamlit as st
import functions
todos = functions.read_todos()


def add_todo():
    new_todo = st.session_state["new_todo"] + "\n"
    todos.append(new_todo.capitalize())
    functions.write_todos(todos)


st.title("My todo App")
st.subheader("This app is created to increase productivity.")
st.write("You can manage a simple todo list with this App")

todos = functions.read_todos()
for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()


st.text_input(label="Enter a Todo:", label_visibility='visible', placeholder="Add a todo item ...",
              on_change=add_todo, key='new_todo')

# print(st.session_state["new_todo"])
# st.session_state

# check if the text_input can be stores in a variable
# st.write(text_input) # This works
