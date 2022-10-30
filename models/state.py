#!/usr/bin/python3
'''State that inherits from BaseModel'''
from models.base_model import BaseModel


class State(BaseModel):
    '''Base class for state models'''
    name = ""

    def __init__(self, *args, **kwargs):
        '''Inititalize class'''
        super().__init__(*args, **kwargs)
