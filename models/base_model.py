""" AirBnb project - BaseModel class """

import uuid
from datetime import datetime
import models


class BaseModel:
    """ This class defines all common attributes/methods for other classes """
    def __init__(self, *args, **kwargs):
        """ method constructor """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if kwargs:
            form = "%Y-%m-%dT%H:%M:%S.%f"
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                    continue
                if key == "created_at":
                    self.created_at = datetime.strptime(value, form)
                    continue
                if key == "updated_at":
                    self.updated_at = datetime.strptime(value, form)
                    continue
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """ print a readable string """
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """ updates with the current datetime """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary representation of all attributes."""
        d = self.__dict__
        d["created_at"] = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")#datetime.isoformat(self.created_at))
        d["updated_at"] = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")#datetime.isoformat(self.updated_at))
        d["__class__"] = self.__class__.__name__
        return (d)
