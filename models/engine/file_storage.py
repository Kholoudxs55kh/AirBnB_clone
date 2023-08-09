#!/usr/bin/python3
"""AirBnb Clone Project , This File Contains The
Class "FileStorage" to manipulate the Data with
"""


class FileStorage:
    """The Parent Class For Storaging"""
    __file_path = 'Aras.Json'
    __objects = {}

    def all(self):
        """returns The Dict Objs"""
        return FileStorage.__objects

    def new(self, obj):
        """## sets ## in __objects the obj with key
        should be printed like this:
        'BaseModel.ee49c413-023a-4b49-bd28-f2936c95460d' as key : {value}
        className.id: {dict containing all att including id again}
        """
        """ ### SETS no Return ###
        ==> the key of the ___objects would be the return Value,
        as i understand, it would return a dic containg all the att for
        that user using the id"""
#        obj = FileStorage._objects[obj.type(self).__name_ + "." + str(obj.id)]
        obj = FileStorage._objects[obj.__class.__name_ + "." + str(obj.id)]

    def save(self):
        """serializes __objects to the json file"""
        pass

    def passreload( self):
        """ deserializes the Json file to dict"""
