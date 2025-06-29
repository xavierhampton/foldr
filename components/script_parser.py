import os

class Parser:
    def __init__(self):
        self.scriptPath = '../config.txt'
        if not os.path.exists(self.scriptPath):
            raise FileNotFoundError(f"Script file not found: {self.scriptPath}")
        


    def run(self):
        return self._parse_script()

    def _parse_script(self):
        with open(self.scriptPath, 'r') as file:
            lines = file.readlines()

