#!/usr/bin/python3
"""serializes instances to a JSON file and deserializes
JSON file to instances"""
import json


class FileStorage:
    """serializes instances to a JSON file and
    deserializes JSON file to instances"""
    __file_path = "file.json"
    __objects = dict()

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = obj.__class__.__name__ + '.' + obj.id
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        with open(self.__file_path, 'w') as f:
            obj = {key: obj.to_dict() for key, obj in self.__objects.items()}
            json.dump(obj, f)

    def reload(self):
        """deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists ; otherwise, do nothing. If the
        file doesn’t exist"""
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                self.__objects = json.load(f)
        except FileNotFoundError:
            pass
