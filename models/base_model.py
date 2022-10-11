#!/usr/bin/python3
"""BaseModel"""
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
            
    def __str__(self):
        return "[{}] ({}) ({})".format(self.__class__.__name__, self.id, self.__dict__)
    
    def save(self):
        """updates the public instance attribute updated_at with the current datetime"""
        self.updated_at = datetime.now()
        
    def to_dict(self):
        """returns a dictionary containing all keys/values"""
        self.__dict__['__class__'] = self.__class__.__name__
        self.__dict__['updated_at'] = datetime.isoformat(self.__dict__['updated_at'])
        self.__dict__['created_at'] = datetime.isoformat(self.__dict__['created_at'])
        return (self.__dict__)