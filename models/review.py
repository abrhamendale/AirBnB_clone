#!/usr/bin/python3
"""State module"""
from models.base_model import BaseModel


class Review(BaseModel):
    """State class"""
    place_id = ""
    user_id = ""
    text = ""
