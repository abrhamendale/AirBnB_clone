#!/usr/bin/python3
"""Base model module"""
import uuid
from models.__init__ import storage
from datetime import datetime


class BaseModel:
    """BaseModel class"""
    id = ""
    created_at = datetime.now()
    updated_at = datetime.now()

    def __init__(self, *args, **kwargs):
        """Initializes basemodel instances."""
        if kwargs and not __class__:
            for i in kwargs.keys():
                #print(i, type(i))
                if i not in ["created_at", "updated_at"]:
                    setattr(self, i, kwargs[i])
                else:
                    self.created_at = datetime.strptime(kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                    self.updated_at = datetime.strptime(kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
        else:
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            self.id = str(uuid.uuid4())
            storage.new(self)

    def __str__(self):
        """Returns the stringrepresentation of a class."""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates the updated_at variable."""
        self.updated_at = datetime.now()#.strftime("%Y-%m-%dT%H:%M:%S.%f")
        keys = self.id
        keys = self.__class__.__name__ + "." + keys
        (storage.objects)[keys]["updated_at"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
        storage.save()
        #self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary representation of all attributes."""
        d = self.__dict__
        d["created_at"] = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")#datetime.isoformat(self.created_at))
        d["updated_at"] = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")#datetime.isoformat(self.updated_at))
        d["__class__"] = self.__class__.__name__
        return (d)
