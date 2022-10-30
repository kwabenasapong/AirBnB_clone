#!/usr/bin/python3
'''Review that inherits from BaseModel'''
from models.base_model import BaseModel


class Review(BaseModel):
    '''Base class for review models'''
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        '''Inititalize class'''
        super().__init__(*args, **kwargs)
