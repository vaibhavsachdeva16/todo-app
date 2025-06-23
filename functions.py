def get_todos(filepath='todos.txt'):
    """
    Read a text file and return the list of
    to-do items.
    """
    with open(filepath, 'r') as file:
        todos_local = file.readlines()
    return todos_local


def write_todos(todos_arg, filepath='todos.txt'):
    """
    Write the to-do items list in the text file.
    """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

# only when this file is run it's name is main.
# If it is run from other files or imported then it's name is functions (what it's name is)
# print(__name__)


if __name__ == "__main__":
    print("Hello")
    print(get_todos())
