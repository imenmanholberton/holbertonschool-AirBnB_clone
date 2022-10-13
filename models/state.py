#!/usr/bin/python3
"""State Class"""
from models.base_model import BaseModel

class State(BaseModel):
    name = "inherited class State from BaseModel"
    
    def __init__(self, *args, **kwargs):
        """constructor"""
        super().__init__(self, *args, **kwargs)