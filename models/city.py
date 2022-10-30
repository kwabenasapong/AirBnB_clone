#!/usr/bin/env python
'''City that inherits from BaseModel'''
from models.base_model import BaseModel


class City(BaseModel):
    '''Base class for city models'''
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        '''Inititalize class'''
        super().__init__(*args, **kwargs)
