#!/usr/bin/python3
""""""
from models.base_model import BaseModel

class Amenity(BaseModel):
    name = ""
    
    def __init__(self, *args, **kwargs):
        """constructor"""
        super().__init__(self, *args, **kwargs)