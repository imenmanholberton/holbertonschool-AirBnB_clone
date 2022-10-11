#!/usr/bin/python3
""""""
import json
from models.base_model import BaseModel
from pathlib import Path

class FileStorage:

    __file_path = "file.json"
    __objects = {}

    def all(self):
        return (FileStorage.__objects)

    def new(self, obj):
        FileStorage.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        dict = {}
        dict.update(FileStorage.__objects)
        for key, value in dict.items():
            dict[key] = value.to_dict()
        with open(FileStorage.__file_path, "w", ) as file:
            json.dump(dict, file)
    
    def reload(self):
        try: 
            if Path("__file_path").exists():
                with open(FileStorage.__file_path, "r") as file:
                    n_dict = json.load(file)
                for key, value in n_dict.items():
                    FileStorage.__objects[key] = BaseModel(**value)
        except IOError:
            pass
