#!/usr/bin/python3
"""State class that inherits from BaseModel"""
from models.base_model import BaseModel


class State(BaseModel):
    """State class"""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initialize the instance attributes"""
        super().__init__(self, *args, **kwargs)
