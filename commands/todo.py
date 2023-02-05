def add_todo_point():
    todo_to_add = input("What do you want to add?:")
    with open("UserDataStorage/todo_list.txt", "a+") as file:
        file.write(f"{todo_to_add}\n")
        file.close()
    print("Addded successfuly!")


def remove_todo_point():
    item = int(input("Which Item do you want to check off?:"))
    content = open("UserDataStorage/todo_list.txt").read().split("\n")
    content.pop(item)
    content_new = '\n'.join(content)
    write(content=content_new)
    print("Checked off!")


def rename_todo_list():
    new_name = input("What should be the new name of you're todo list?:")
    content = open("UserDataStorage/todo_list.txt").read().split("\n")
    content[0] = new_name
    content_new = '\n'.join(content)
    write(content=content_new)
    print("Renamed susuccessfuly!")


def write(content):
    with open("UserDataStorage/todo_list.txt", "w") as file:
        file.write(content)
    file.close()


def show_todo():
    todo_list = open("UserDataStorage/todo_list.txt").read().split("\n")
    todo_list_name = todo_list[0]
    # delets free line and name of list
    todo_list.pop(-1)
    todo_list.pop(0)
    print(f"{todo_list_name}:\n")
    for num, item in enumerate(todo_list):
        print(f"\t{num+1} - {item}")
    print("\n")
