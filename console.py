#!/usr/bin/python3
"""console"""
import cmd
import models
from models.base_model import BaseModel
from models import storage
import shlex
from shlex import split



class HBNBCommand(cmd.Cmd):
    
    """hbnb promt"""
    prompt = '(hbnb) '

    def do_quit(self, arg) :
        return  True

    def do_EOF(self, arg):
        print()
        return True

    def emptyline(self):
        pass

    def create (self, arg):
        """create a new instance of BaseModel"""
        if arg == "":
            print("** class name missing **")
        List = arg.split()
        try:
            obj = eval(List[0])()
            print(obj.id)
            obj.save()
        except:
            print("** class doesn't exist **")
    def show(self, arg):
        """show object by id"""
        if arg == "":
            print("** class name missing **")
        List = parse(arg)
        try:
            obj = eval(List[0])()
        except:
            print("** class doesn't exist **")
        if len(List) == 1:
            print("** instance idmisiing **")
        check = False
        for key, value in storage.all().items():
            if key == "{}.{}".format(List[0],List[1]):
                print(value)
                check = True
            if check == False:
                print ("**no instance")

def parse(arg):
        return shlex.split(arg)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
