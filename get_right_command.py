from commands.test import test
from commands.read_backwards import read_backwards
from commands.calculator import calculator
from commands.translate import translate
from commands.message_pop_up import send_notification


class GetRightCommand:
    def __init__(self):
        self.commands = {
            "test": test,
            "read backwards": read_backwards,
            "calculator": calculator,
            "translate": translate,
            "pop-up notification": send_notification
        }

    def setup(self, user_input):
        self.user_inp = user_input

    def find_command(self):
        if self.user_inp in self.commands.keys():
            self.commands[self.user_inp]()
        else:
            print(f"Command '{self.user_inp}' not found.")


if __name__ == "__main__":

    rightcommand = GetRightCommand()
    rightcommand.setup(input(">>Command:"))
    rightcommand.find_command()