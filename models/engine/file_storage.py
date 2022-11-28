#!/usr/bin/python3
""" FileStorage Class - serializes and deserializes JSON file to instances """

import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
import models


class FileStorage:
    """ This class serializes and deserializes JSON files """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """ Method returns the dictionary __objects """
        return self.__objects

    def new(self, obj):
        """ sets in __objects the obj with class name and id """
        new_1 = obj.__class__.__name__
        new_2 = obj.id
        new = new_1 + '.' + new_2
        self.__objects[new] = obj

    def save(self):
        """ serialization """
        dict_add = {}
        with open(self.__file_path, 'w') as f:
            for key, value in self.__objects.items():
                dict_add[key] = value.to_dict()
            json.dump(dict_add, f)

    def reload(self):
        """ deserialization """
        classes = {'BaseModel': BaseModel,
                   'User': User, 'Place': Place,
                   'State': State, 'City': City,
                   'Amenity': Amenity, 'Review': Review}
        try:
            with open(self.__file_path, 'r') as f1:
                file_store = json.load(f1)
                for key, value in file_store.items():
                    if '__class__' in value:
                        val = classes[value['__class__']](**value)
                        self.__objects[key] = val
        except:
            pass
