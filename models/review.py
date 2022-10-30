#!/usr/bin/python3
"""Reeview class that inherits from BaseModel"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review class"""
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """Initialize the instance attributes"""
        super().__init__(self, *args, **kwargs)
