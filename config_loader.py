import json


class ConfigLoader:
    def __init__(self):
        self.filename = "configs.json"
        self.configs = {}
        self.read_file()

    def read_file(self):
        with open(self.filename, "r") as file:
            self.configs = json.load(file)


if __name__ == "__main__":
    config_loader = ConfigLoader()
