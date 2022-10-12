#!/usr/bin/python3
""""""
import cmd
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """hbnb promt"""

    promt = "(hbnb) "

    classe = {'BaseModel': BaseModel}
    def quit(self, argument):
        exit()

    def EOF(self, argument):
        print()
        exit()

    def emptyline(self):
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
