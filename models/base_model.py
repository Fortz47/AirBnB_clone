#!/usr/bin/python3
"""defines all common attributes/methods for other classes"""
import models
import uuid
from datetime import datetime


class BaseModel:
    """defines all common attributes/methods for other classes"""

    def __init__(self, *args, **kwargs):
        """intialises BaseModel class"""

        tform = "%Y-%m-%dT%H:%M:%S.%f"
        if len(kwargs) != 0:
        for k, v in kwargs.items():
            if k is 'created_at' or k is 'updated_at':
                self.__dict__[k] = datetime.strptime(v, tform)
            else self.__dict__[k] = v
            if key not in ['__class__']:
                    setattr(self, k, v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.today()
            self.updated_at = datetime.today()

    def save(self):
        """updates the public instance attribute updated_at with the
        current datetime"""
        self.updated_at = datetime.today()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__
        of the instance
        """

        dict_rep = self.__dict__.copy()
        dict_rep['created_at'] = self.created_at.isoformat()
        dict_rep['id'] = self.id
        dict_rep['updated_at'] = self.updated_at.isoformat()
        dict_rep['__class__'] = self.__class__.__name__
        return dict_rep

    def __str__(self):
        """Return the print/str representation of the BaseModel instance."""
        className = self.__class__.__name__
        return "[{}] ({}) {}".format(className, self.id, self.__dict__)
