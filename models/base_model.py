"""This is the Basemodel for the Airbnb clone project"""
import models
from datetime import datetime
from uuid import uuid4
import json


class BaseModel:
    """BaseModel class"""
    def __init__(self, *args, **kwargs):
        """Using kwargs for the constructor of a Basemodel
            *args: will not be used

            If its a new instance, instantiate with the following:
            Args:
                id: The unique ID for the instance
                created_at: The time the instance is created
                updated_at: The time the instancve is updated
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key == "__class__":
                    continue
                setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Magic method to print the Instance"""
        cls = self.__class__.__name__
        return "[{}] ({}) {}".format(cls, self.id, self.__dict__)

    def save(self):
        """Update 'updated_at' with the current time"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns dictionary containing all attributes"""
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict
