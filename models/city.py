#!/usr/bin/python3
"""City class that inherits from BaseModel"""
from models.base_model import BaseModel


class City(BaseModel):
    """City class"""
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initialize the instance attributes"""
        super().__init__(self, *args, **kwargs)
