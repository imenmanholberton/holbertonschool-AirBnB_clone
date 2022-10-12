#!/usr/bin/python3
"""console"""
import cmd
from models.base_model import BaseModel
import sys

class HBNBCommand(cmd.Cmd):
    """hbnb promt"""

    prompt = "(hbnb) "

    classe = {'BaseModel': BaseModel}
    def quit(self, arg):
        exit()

    def EOF(self, arg):
        print()
        exit()

    def emptyline(self):
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
