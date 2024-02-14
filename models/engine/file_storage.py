#!/usr/bin/python3
"""
Module: file_storage.py

Defines the FileStorage class, which serializes instances to a JSON file
and deserializes JSON file to instances.
"""
import json
from models.base_model import BaseModel


class FileStorage:
    """ instances to a JSON file and deserializes JSON file to instances"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(
            type(obj).__name__, obj.id
        )
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        serialized_objs = {}
        for key, obj in self.__objects.items():
            serialized_objs[key] = obj.to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(serialized_objs, file)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r') as file:
                serialized_objs = json.load(file)
                for key, obj_data in serialized_objs.items():
                    class_name, obj_id = key.split('.')
                    class_ = eval(class_name)  # Convert string to class
                    obj = class_(**obj_data)   # Create instance of class
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass
