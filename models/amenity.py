#!/usr/bin/python3
"""Amenity class that inherits from BaseMOdel"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class"""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initialize the instance variable"""
        super().__init__(self, *args, **kwargs)
