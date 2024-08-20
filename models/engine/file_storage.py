#!/usr/bin/python3
"""
FileStorage class that serializes instances to a JSON file
and deserializes JSON file to instances.
"""

import json
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """Serializes instances to a JSON file and deserializes them back."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        if obj is None:
            return
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file."""
        with open(self.__file_path, 'w') as f:
            json_objects = {k: v.to_dict() for k, v in self.__objects.items()}
            json.dump(json_objects, f)

    def reload(self):
        """Deserializes the JSON file to __objects if it exists."""
        try:
            with open(self.__file_path, 'r') as f:
                json_objects = json.load(f)
                for obj_dict in json_objects.values():
                    cls_name = obj_dict['__class__']
                    if cls_name == "BaseModel":
                        obj = BaseModel(**obj_dict)
                    elif cls_name == "User":
                        obj = User(**obj_dict)
                    else:
                        continue
                    self.new(obj)
        except FileNotFoundError:
            pass
