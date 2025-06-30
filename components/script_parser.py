import os

class Parser:
    def __init__(self):
        self.scriptPath = '../config.txt'
        if not os.path.exists(self.scriptPath):
            raise FileNotFoundError(f"Script file not found: {self.scriptPath}")
        
        self.documentStructure = []
    
    def run(self):
        return self._parse_script()

    def _parse_script(self):
        with open(self.scriptPath, 'r') as file:
            lines = file.readlines()

            res = []
            current_section = []

            for line in lines:
                if line.startswith('/'): continue  # Skip comments
                if line.startswith('-'):
                    if current_section:
                        res.append(current_section)
                    current_section = [line.strip()]
                else:
                    current_section.append(line.strip())
                
            return res
