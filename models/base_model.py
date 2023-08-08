#!/usr/bin/python3
"""AirBnb Clone Project m This File Contains The Main
Class "BaseModel" For The Project
"""
import uuid
from datetime import datetime


class BaseModel:
    """The Parent Class For This Project
    """
    def __init__(self):
        """ The Class Constructor """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """ Print a Readable String"""
        return "[{}] ({}) {}".format(type(self).__name__,
                                     self.id, self.__dict__)

    def save(self):
        """ updates the public instance attribute updated_at
        with the current datetime"""

        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary containing all keys/values
        of __dict__ of the instance"""
        my_dict = self.__dict__.copy()
        my_dict['__class__'] = type(self).__name__
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()

        return my_dict
