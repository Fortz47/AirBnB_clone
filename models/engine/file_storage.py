#!/usr/bin/python3
"""serializes instances to a JSON file and deserializes
JSON file to instances
"""



class FileStorage:
    """serializes instances to a JSON file and deserializes
    JSON file to instances"""
    __file_path = 'file.json'
    __objects = {}

    def all(self):
            return self.__objects

    def new(self, obj):
        clname = obj.__class__.__name__.id
        self.__object[clname] = 

    def save(self):
        self.__file_path.json.dumps(self.__objects)
