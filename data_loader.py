import json


class DataLoader:
    def __init__(self):
        self.filename = "configs.json"
        self.configs = {}
        self.read_file()

    def read_file(self):
        with open(self.filename, "r") as file:
            self.configs = json.load(file)
        file.close()

        with open(self.configs.get("reaction_filename"), "r") as file:
            self.reactions = json.load(file)
        file.close()


if __name__ == "__main__":
    data_loader = DataLoader()
