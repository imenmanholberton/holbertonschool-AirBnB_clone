#!/usr/bin/python3
"""console Airbnb project"""
from datetime import datetime
import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
from shlex import split
from models.user import User
from models.place import  Place
from models.state import State
from models.city import City
from models.amenity import  Amenity
from models.review import Review
from models import classes

import cmd


class HBNBCommand(cmd.Cmd):
    
    """hbnb promt"""
    prompt = '(hbnb) '
    clss = classes

    def emptyline(self):
        pass

    def do_create (self, arg):
        """create a new instance of BaseModel"""
        if arg == "":
            print("** class name missing **")
            return
        List = arg.split()

        try:
            obj = eval(List[0])()
            obj.save()
            print(obj.id)
        except:
            print("** class doesn't exist **")
    def do_show(self, arg):
        """show object by id"""
        List = arg.split()
        if arg == "":
            print("** class name missing **")
            return
        if len(List) == 1:
            print("** instance id missing **")
            return
        try:
            eval(List[0])()
        except:
            print("** class doesn't exist **")
        
        obj = storage.all()
        key = List[0]  +   "." +  List[1]

        try:
            value = obj[key]
            print(value)
        except KeyError:
            print("** instance id missing **")

    def do_destroy(self, arg):
        """Delte an instance based on the class name"""
        List = arg.split()
        if arg == "":
            print("** class name missing **")
            return
        if len[list] == 1:
            print("** instance id missing **")
        try:
            eval(List[0])
        except:
            print("** class doesn't exist **")
        obj = storage.all()
        key = List[0] +  "." + List[1]

        try:
            del obj[key]
        except:
            print("** no instance found **")
        storage.save()
    
    
    def do_all(self, arg):
        """Prints all string representation of all instances based
        or not on the class name"""
        List = arg.split()
        if List[0] not in classes:
            print("** class doesn't exist **")
        else:
            newList = []
            for key, value in  storage.all().items():
                if value.__class__.__name__== List[0]:
                    newList += [value.__str__()]
            print(newList)

    def do_update(self, arg):
        """pdate an objject by className and id, with attribute and value"""
        if not arg:
            print("** class name missing **")
            return
        Lists = arg.split(" ")
        Objts =  storage.all()
        if Lists[0] in self.clss:
            if len(Lists) < 2:
                print("** instance id missing **")
                return
            v = Lists[0] + "." + Lists[1]
            if v not in Objts:
                print("** no instance found **")
            else:
                obj = Objts[v]
                attrbte  = ["id", "created_at", "updated_at"]
                if obj:
                    List = arg.split(" ")
                    if len(List) < 3:
                        print("** attribute name missing **")
                    elif len(List) < 4:
                        print("** value missing **")
                    elif List[2] not in attrbte:
                        obj.__dict__[List[2]] = List[3]
                        obj.updated_at = datetime.now()
                        storage.save()
        else:
            print("** class doesn't exist **")
    
    def do_quit(self, arg) :
        """quit command"""
        return  True

    def do_EOF(self, arg):
        """end of file"""
        print()
        return True



if __name__ == '__main__':
    HBNBCommand().cmdloop()
