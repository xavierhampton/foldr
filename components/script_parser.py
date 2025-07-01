import os

class Parser:
    #Checks if path exists for config file
    def __init__(self, scriptPath=None):
        self.scriptPath = scriptPath
        if not os.path.exists(self.scriptPath):
            raise FileNotFoundError(f"Script file not found: {self.scriptPath}")
    
    #Runs the script parser, returns a list of tuples with file names and their parent directories
    def run(self):
        return self._parse_script()

    #Private method for parsing script file
    def _parse_script(self):
        with open(self.scriptPath, 'r') as file:
            lines = file.readlines()

            res = []
            parent = ""

            for line in lines:
                # Skip comments
                if line.startswith('/'): continue  

                #Folders
                if line.startswith('-'):
                    parent = line.strip().replace('-', '')
                    
                #File Placeholders
                elif (len(line.strip()) > 0):
                    res.append((line.strip(), parent))

            return res

