#!/usr/bin/python3
"""AirBnb Clone Project , This File Contains The
Class "FileStorage" to manipulate the Data with
"""
import json
from models.base_model import BaseModel
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """The Parent Class For Storaging"""
    __file_path = 'Aras.json'
    __objects = {}

    def all(self):
        """returns The Dict Objs"""
        return FileStorage.__objects

    def new(self, obj):
        """## sets ## in __objects the obj with key
        should be printed like this:
        'BaseModel.ee49c413-023a-4b49-bd28-f2936c95460d' as key : {value}
        className.id: {dict containing all att including id again}
        ### SETS no Return ###
        ==> the key of the ___objects would be the return Value,
        as i understand, it would return a dic containg all the att for
        that user using the id"""
# obj = FileStorage.__objects[obj.type(self).__name__ + "." + str(obj.id)]
        FileStorage.__objects[obj.__class__.__name__ + "." + str(obj.id)] = obj

    def save(self):
        """serializes __objects to the json file"""
        my_dict = {}
        with open(FileStorage.__file_path, 'w') as f:
            for key, value in FileStorage.__objects.items():
                # calling to_dict because of new method format|^|
                my_dict[key] = value.to_dict()
            json.dump(my_dict, f)

    def reload(self):
        """deserializes the Json file to dict"""
        f = FileStorage.__file_path
#        if  isinstance(f, file) and (f):
        try:
            Data = {}
            if os.path.isfile(f):   # googled
                with open(f, 'r') as fi:
                    Data = json.load(fi)
                    # need to reset the values!! val containing all keys & vals
                    for val in Data.values():
                        class_val = val["__class__"]
                        self.new(eval(class_val)(**val))

        except FileNotFoundError:
            pass
