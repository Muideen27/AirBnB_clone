#!/usr/bin/env python3
"""Amenity class, a class that inherit BaseModel class"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """A subclass of BaseModel class
    public class attribute:
        name: (str)
    """
    name = ""
