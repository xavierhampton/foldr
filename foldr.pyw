import os
import shutil
import components.script_parser as sc

#Path to the organization folder
# This is the folder where all the files and folders will be organized
ORG_PATH = "C:\\Users\\xavie\\Downloads"


# foldr.pyw - Main application file for Foldr
class application:
    # Application class for Foldr
    # This class initializes the application, checks for the organization path,

    def __init__(self):
        self.name = "Foldr Application"

        if not os.path.exists(ORG_PATH):
            raise FileNotFoundError(f"Organization path does not exist: {ORG_PATH}")

        self.root_folder = os.path.dirname(os.path.abspath(__file__))

        self.parser = sc.Parser(self.root_folder + "/config.txt")
        self.organization = self.parser.run()

    # Checks if the folder exists, if not, creates it
    # Returns True if the folder was created, False if there is error
    def check_folder_exists(self, folder_path):
        if not os.path.exists(folder_path):
            try:
                os.mkdir(folder_path)
                return True
            except Exception as e:
                raise FileNotFoundError(f"Folder does not exist, folder creation error: {folder_path}, Error: {e}")
        return False
    
    def find_org_folder(self, entry):
        # Finds the organization folder based on the entry name
        # Returns the path to the organization folder
        for org, folder in self.organization:
            if (org.startswith("*.") and entry.lower().endswith(org.lower()[2:])):
                org_folder = os.path.join(ORG_PATH, folder)
                if not os.path.exists(org_folder):
                    self.check_folder_exists(org_folder)
                return org_folder
            
        return None

    # Runs the application
    def run(self):
        print(f"Running application: {self.name}")
        entries = os.listdir(ORG_PATH)

        for entry in entries:
            folder = self.find_org_folder(entry)
            print(folder)

        
        print(self.organization)


application = application().run()