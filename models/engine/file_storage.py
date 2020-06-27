#!/usr/bin/python3
"""FileStorage class module"""
import json
from models.base_model import BaseModel


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        keyobj = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(keyobj, obj.id)] = obj

    def save(self):
        dicobj = FileStorage.__objects
        objdic = {obj: dicobj[obj].to_dict() for obj in dicobj.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdic, f)

    def reload(self):
        try:
            with open(FileStorage.__file_path) as f:
                objdic = json.load(f)
                for value in objdic.values():
                    cls_name = value["__class__"]
                    del value["__class__"]
                    self.new(eval(cls_name)(**value))
        except FileNotFoundError:
            return
