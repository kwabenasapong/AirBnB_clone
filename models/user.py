#!/usr/bin/python3
"""Creating The first user class"""
from models.base_model import BaseModel


class User(BaseModel):
    """User class that inherits from BaseModel"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """Initialize the instance attributes"""
        super().__init__(self, *args, **kwargs)
