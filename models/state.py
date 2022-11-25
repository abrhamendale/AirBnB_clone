#!/usr/bin/python3
"""State module"""
from models.base_model import BaseModel


class State(BaseModel):
    """State class"""
    name = ""

    def __init__(self):
        """Initializes new user instances"""
        super(State, self).__init__()
