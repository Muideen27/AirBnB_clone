#!/usr/bin/env python3
"""Module for FileStorage class"""


import json
import datetime
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models.state import State


class FileStorage:
    """class for serialization and deserialization of base model"""
    __file_path = "file.json"
    __objects = {}
    __classes = {"User": User, "Amenity": Amenity, "Place": Place, "City":
                 City, "State": State, "BaseModel": BaseModel}

    def all(self):
        """
        Returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """sets in  __objects the obj with key <obj class name>.id"""
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        dict_obj = {}
        for key, value in self.__objects.items():
            dict_obj[key] = value.to_dict()
        with open(self.__file_path, mode="w", encoding="utf-8") as f:
            json.dump(dict_obj, f)

    def reload(self):
        """
        deserializes the JSON file to __objects (only if the JSON
        file (__file_path)
        exists ; otherwise, do nothing. If the file doesn’t exist,
        no exception should be raised)
        """
        try:
            with open(self.__file_path, mode="r", encoding="utf-8") as f:
                dict_obj = json.load(f)
                for key, value in dict_obj.items():
                    class_name, obj_id = key.split(".")
                    cls = globals()[class_name]
                    obj = cls(**value)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass
