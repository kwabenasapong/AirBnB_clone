#!/usr/bin/env python
'''User that inherits from BaseModel'''
from models.base_model import BaseModel

class User(BaseModel):
        '''Base class for user models'''
        email = ""
        password = ""
        first_name = ""
        last_name = ""

        def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)