#!/usr/bin/python3
"""State module"""
from models.__init__ import storage
from models.base_model import BaseModel


class Amenity(BaseModel):
    """State class"""
    name = ""

    def __init__(self):
        """Initializes new user instances"""
        super(Amenity, self).__init__()
