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
                for o in objdic.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return
