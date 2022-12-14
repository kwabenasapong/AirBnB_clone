#!/usr/bin/python3
"""Filestorage class """
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage():
    """Filestorage class"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary"""
        return FileStorage.__objects

    def new(self, obj):
        """sets obj with its key in __objects"""
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """serialize __objects to json"""
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            new_dict = FileStorage.__objects.copy()
            for k, v in FileStorage.__objects.items():
                new_dict[k] = v.to_dict()
            json.dump(new_dict, f)

    def reload(self):
        """Deserialize the JSON in __file_path if it exists"""
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                loaded = json.load(f)
                for base_dict in loaded.values():
                    name = base_dict["__class__"]
                    del base_dict["__class__"]
                    self.new(eval(name)(**base_dict))
        except FileNotFoundError:
            return
