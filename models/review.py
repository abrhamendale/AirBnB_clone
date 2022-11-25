#!/usr/bin/python3
"""State module"""
from models.__init__ import storage
from models.base_model import BaseModel


class Review(BaseModel):
    """State class"""
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self):
        """Initializes new user instances"""
        super(Review, self).__init__()
