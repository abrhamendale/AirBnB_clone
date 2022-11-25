#!/usr/bin/python3
"""State module"""
from models.__init__ import storage
from models.base_model import BaseModel


class City(BaseModel):
    """State class"""
    state_id = ""
    name = ""

    def __init__(self):
        """Initializes new user instances"""
        super(City, self).__init__()
