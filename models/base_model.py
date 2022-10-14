#!/usr/bin/python3
"""BaseModel"""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """repmresen class"""
    def __init__(self, *args, **kwargs):
        """
        attr(id): objectid
        attr(created_at): datetime - assign with the current datetime when an instance is created
        attr(updated_at): datetime - assign with the current datetime when an instance is created and it will be updated
        every time you change your object
        """
        if len(kwargs)  != 0:
            for key, value in kwargs.items():
                if key == "created_at" or  key == "updated_at":
                    obj = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, obj)
                elif key != "__class__":
                    setattr(self, key, value)
        
        else:
            self.id = str(uuid4())
            self.created_at =  datetime.now()
            self.updated_at= datetime.now()
            models.storage.new(self)
    def __str__(self):
        return "[{}] ({}) ({})".format(self.__class__.__name__, self.id, self.__dict__)
    
    def save(self):
        """updates the public instance attribute updated_at with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()
        
    def to_dict(self):
        """returns a dictionary containing all keys/values"""
        newdict = self.__dict__.copy()
        newdict['__class__'] = self.__class__.__name__
        newdict['updated_at'] = self.updated_at.isoformat()
        newdict['created_at'] = self.created_at.isoformat()
        return newdict