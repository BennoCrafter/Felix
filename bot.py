import json
from get_right_command import GetRightCommand


class ChatBot:
    def __init__(self):
        print("Welcome to Felix!")
        # objects

        self.command_finder = GetRightCommand()

        self.json_file = "conversation_data.json"

        with open(self.json_file, 'r') as file:
            self.data = json.load(file)
        file.close()

        self.user_input = ""
        print("""
           _____                                          
          /     \\     How can i help you?                                        
         |   0 0 |                                        
         |   \_/ |                                        
          \\_____/                                          
        """)

    def make_decision(self, user_input):
        self.get_output_of_data(user_input=user_input)

    def get_output_of_data(self, user_input):
        conversation_response = False
        for pattern in self.data['patterns']:
            for keyword in pattern['keywords']:
                if keyword in user_input.lower():
                    print("Chatbot: " + pattern['response'])
                    conversation_response = True
        if not conversation_response:
            if user_input in self.command_finder.commands.keys():
                self.command_finder.setup(user_input=user_input)
                self.command_finder.find_command()
            else:
                print("Something went wrong!")


if __name__ == "__main__":
    chat_bot = ChatBot()

    while chat_bot.user_input != "exit":
        chat_bot.make_decision(user_input=input("User: "))
