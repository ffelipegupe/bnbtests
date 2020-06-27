#!/usr/bin/python3
"""BaseModel Class module"""
import models
from datetime import datetime
from uuid import uuid4


class BaseModel:
    def __init__(self, *args, **kwargs):
        if kwargs:
            self.id = kwargs.get('id')
            ca = datetime.strptime(kwargs.get('created_at'), '%Y-%m-%dT%H:%M:%S.%f')
            self.created_at = ca
            ua = datetime.strptime(kwargs.get('updated_at'), '%Y-%m-%dT%H:%M:%S.%f')
            self.updated_at = ua
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()


    def __str__(self):
        a = type(self).__name__
        b = self.id
        c = self.__dict__
        return "[{}] ({}) {}".format(a, b, c)

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        self.__dict__['__class__'] = type(self).__name__
        self.__dict__['created_at'] = self.created_at.isoformat()
        self.__dict__['updated_at'] = self.updated_at.isoformat()
        return self.__dict__