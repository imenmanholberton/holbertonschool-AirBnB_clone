#!/usr/bin/python3
""""""
import json
from models.base_model import BaseModel


class FileStorage:

    __file_path = "file.json"
    __objects = {}

    def all(self):
        return (self.__objects)

    def new(self, obj):
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        dict = {}
        for key in self.__objects():
            dict[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w', ) as file:
            json.dump(dict, file)
    
    def reload(self):
        try: 
            with open(self.__file_path, 'r', encoding="UTF_8") as file:
                n_dict = json.load(file)
                for key, value in n_dict.items():
                    attr = eval(value["__class__"])(**value)
                    self.__objects[key] = attr
        except IOError:
            pass
