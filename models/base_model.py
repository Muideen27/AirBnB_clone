#!/usr/bin/env python3
"""Custom Base class for the entire project
"""

import uuid
from datetime import datetime
import models

class BaseModel:

    """Custom base for all the classes in the AirBnb console project
    Arttributes:
        id(str): handles unique user identity
        created_at: assigns current datetime
        updated_at: updates current datetime
    Methods:
        __str__: prints the class name, id, and creates dictionary
        representations of the input values
        save(self): updates instance arttributes with current datetime
        to_dict(self): returns the dictionary values of the instance obj
    """

    def __init__(self, *args, **kwargs):
        """Instantiation of a Base instance

        Args:
            - *args: list of ordinary arguments
            - **kwargs: dict of key-values arguments
        """

        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime(value,
                                                         "%Y-%m-%dT%H:%M:%S.%f"))
                elif key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
            Returns string representation of the class
        """
        return "[{}] ({}) {}".\
            format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """
            Updates the public instance attributes
            "updates_at" - with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
            Method returns a dictionary containing all keys/value of
            __dict__ instance
        """
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = type(self).__name__
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        return my_dict
