#!/usr/bin/python3
"""Base model module"""
import uuid
from datetime import datetime


class BaseModel:
    """BaseModel class"""
    id = ""
    created_at = 0
    updated_at = 0

    def __init__(self):
        """Initializes basemodel instances."""
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.id = str(uuid.uuid4())
        print(self.created_at)

    def __str__(self):
        """Returns the stringrepresentation of a class."""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates the updated_at variable."""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary representation of all attributes."""
        d = self.__dict__
        d["created_at"] = datetime.isoformat(self.created_at)
        d["updated_at"] = datetime.isoformat(self.updated_at)
        d["__class__"] = self.__class__.__name__
        return (d)
