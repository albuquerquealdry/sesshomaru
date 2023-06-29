import sys
import os
import json

class CustomCommads():
    def __init__(self):
        with open("/home/aldryalbuquerque/sesshomaru/src/ini/custom.json") as custom:
            commandList = custom.read()
        self.commandOrder = json.loads(commandList)
    def callCommand(self, comando):
        teste = self.commandOrder[f"{comando}"]
        os.system(f"{teste}")