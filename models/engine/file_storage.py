#!/usr/bin/python3
"""File storage module"""
import json
import os

class FileStorage:
    """FileStorage class"""

    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        """Initializes new storage instances."""

    @property
    def objects(self):
        """Getter for objects\n"""
        return self.__objects

    @objects.setter
    def objects(self, val):
        """Setter for objects\n"""
        self.__objects = val

    def all(self):
        """Returns a dictionary of __objects."""
        return (self.__objects)
    
    def new(self, obj):
        """sets __objects with key classname.id."""
        keys = obj.id
        keys = obj.__class__.__name__ + "." + keys
        (self.__objects)[keys] = obj.to_dict()

    def save(self):
        """Serializes objects to the JSON filepath."""
        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(self.__objects, f)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        if os.path.isfile(self.__file_path) and os.path.getsize(self.__file_path) != 0:
            with open(self.__file_path, "r", encoding="utf-8") as f:
                self.__objects = json.load(f)
        else:
            pass
    """
    def show(self, c, j):
        "Prints dictionary corrsponding to id."
        key = j
        key = c + "." + key
        return f"[{c}] ({(self.__objects[key])['id']}) {self.__objects[key]}"
    """

    """
    def destroy(self, c, j):
        "Prints dictionary corrsponding to id."
        key = j
        key = c + "." + key
        del self.__objects[key]
        self.save()
    """

    #def all(self, line):
    #    """Prints all instances."""
    #    a = []
    #    for key in self.__objects.keys():
    #        a.append(f"[{line}] ({(self.__objects[key])['id']}) {self.__objects[key]}")
    #    return (a)
