#!/usr/bin/env python3
"""Review class i nherirted from BaseModel"""

from models.base_model import BaseModel


class Review(BaseModel):
    """a class inherited from BaseModel"""

    place_id = ""
    user_id = ""
    text = ""
