from commands.commands_info import commands_info
from commands.get_length import get_length
from commands.test import test
from commands.read_backwards import read_backwards
from commands.todo import *
from commands.translate import translate
from commands.message_pop_up import send_notification
from commands.show_commits import show_commits
from commands.tree import generate_tree
from commands.math_interpreter.calculator import calculate


class GetRightCommand:
    def __init__(self):
        self.commands = {
            "test": test,
            "read backwards": read_backwards,
            "translate": translate,
            "pop-up notification": send_notification,
            "commands": commands_info,
            "show todo": show_todo,
            "add todo": add_todo_point,
            "rename todo": rename_todo_list,
            "check off todo": remove_todo_point,
            "add notification todo": add_notification_todo,
            "show git commits": show_commits,
            "directory tree": generate_tree,
            "get length": get_length,
            "calculate": calculate
        }

    def setup(self, user_input):
        self.user_inp = user_input

    def find_command(self):
        if self.user_inp in self.commands.keys():
            # check if it's a special command
            if self.user_inp == "commands":
                print(f"The current commands are: {list(self.commands.keys())}")
            else:
                self.commands[self.user_inp]()
        else:
            print(f"Command '{self.user_inp}' not found.")


if __name__ == "__main__":
    rightcommand = GetRightCommand()
    rightcommand.setup(input(">>Command:"))
    rightcommand.find_command()