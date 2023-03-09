#!/usr/bin/env python3
"""User class inherited from BaseModel"""


from models.base_model import BaseModel
import json


class User(BaseModel):
    """A class user that inherit from the BaseModel"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
