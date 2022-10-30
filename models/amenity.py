#!/usr/bin/env python
'''Amenity that inherits from BaseModel'''
from models.base_model import BaseModel


class Amenity(BaseModel):
    '''Base class for amenity models'''
    name = ""

    def __init__(self, *args, **kwargs):
        '''Inititalize class'''
        super().__init__(*args, **kwargs)
