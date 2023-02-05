import json


class AddPattern:
    def __init__(self, filename):
        self.filename = filename
        with open(self.filename, "r") as self.file:
            self.data = json.load(self.file)

    def add(self):
        with open(self.filename, "w") as file:
            json.dump(self.data, file, indent=4)
        file.close()

    def format_input_data(self):
        dict = {}
        keywords = input("What should be the keywords? (Please new keyword after \) : ").split("\\")
        response = input("What should be the response? : ")
        deeper_info = input("Is there any deeper info? (like you can answer with no or yes): ")
        dict["keywords"] = keywords
        dict["response"] = response
        dict["deeper_info"] = deeper_info
        self.data["patterns"].append(dict)


if __name__ == "__main__":
    add = AddPattern(filename="conversation_data.json")
    add.format_input_data()
    add.add()