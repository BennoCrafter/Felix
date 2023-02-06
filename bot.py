import json

from data_loader import DataLoader
from get_right_command import GetRightCommand


class ChatBot:
    def __init__(self):
        print("Welcome to Felix!")
        # objects
        self.command_finder = GetRightCommand()
        self.data_loader = DataLoader()
        self.bot_name = self.data_loader.configs.get("bot_name")
        self.reactions = self.data_loader.reactions
        self.json_file = self.data_loader.configs.get("conversation_data_filename")
        self.user_input = ""

        print(self.reactions.get("start"))

    def read_data(self):
        with open(self.json_file, 'r') as file:
            self.data = json.load(file)
        file.close()

    def make_decision(self, user_input):
        self.update()
        if user_input:
            self.get_output_of_data(user_input=user_input)

    def update(self):
        print("Now Update!")

    def get_output_of_data(self, user_input):
        self.user_input = user_input
        possible_responses = ["I'm sorry. I didn't understand it!"]
        conversation_response = False
        for pattern in self.data['patterns']:
            for keyword in pattern['keywords']:
                if keyword in self.user_input.lower():
                    possible_responses.append(pattern['response'])
                    conversation_response = True

        if not conversation_response:
            if self.user_input[0] == "!" and self.user_input.replace("!", "") in self.command_finder.commands.keys():
                self.command_finder.setup(user_input=self.user_input.replace("!", ""))
                self.command_finder.find_command()
        else:
            possible_responses.pop(0)

        print(possible_responses[0])


if __name__ == "__main__":
    chat_bot = ChatBot()
    chat_bot.read_data()

    while chat_bot.user_input != "exit":
        chat_bot.make_decision(user_input=input("User: "))
    # print(chat_bot.reactions.get("end"))