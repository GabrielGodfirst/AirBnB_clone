#!/usr/bin/env python3
"""
Module: base_model.py

Defines the BaseModel class, which provides common attributes
and methods for other classes in the AirBnB application.
"""

import uuid
from datetime import datetime


class BaseModel:
    """Defines common attributes/methods for other classes"""

    def __init__(self):
        """Initialize instance attributes"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Return string representation of the instance"""
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__
        )

    def save(self):
        """Update updated_at attribute with current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Return dictionary representation of the instance"""
        instance_dict = self.__dict__.copy()
        instance_dict['__class__'] = self.__class__.__name__
        instance_dict['created_at'] = self.created_at.isoformat()
        instance_dict['updated_at'] = self.updated_at.isoformat()
        return instance_dict
