#!/usr/bin/python3
"""test for file storage"""
import unittest
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """test the FileStorage
    """
    @classmethod
    def setUpClass(cls):
        """ Setup instance for testing
        """
        cls._model = BaseModel()

    @classmethod
    def tearDown(cls):
        """Remove JSON file (Aras.json) after executing
        """
        del cls._model
        try:
            os.remove("../../../Aras.json")
        except Exception:
            pass

    def test_docstrings(self):
        """Testing docstrings
        """
        self.assertIsNotNone(FileStorage.__doc__)
        self.assertIsNotNone(FileStorage.all.__doc__)
        self.assertIsNotNone(FileStorage.new.__doc__)
        self.assertIsNotNone(FileStorage.save.__doc__)
        self.assertIsNotNone(FileStorage.reload.__doc__)

    def test_all(self):
        """test all method
        """
        storage = FileStorage()
        obj = storage.all()
        self.assertIsNotNone(obj)
        self.assertEqual(type(obj), dict)
        self.assertIs(obj, storage._FileStorage__objects)

    def test_new(self):
        """testing new
        """
        storage = FileStorage()
        obj = storage.all()
        user = User()
        user.id = 123455
        user.name = "Aiko"
        storage.new(user)
        key = user.__class__.__name__ + "." + str(user.id)
        self.assertIsNotNone(obj[key])

    def test_attributes(self):
        """Checks attrs
        """
        self.assertTrue(hasattr(FileStorage, '_FileStorage__objects'))
        self.assertTrue(hasattr(FileStorage, '_FileStorage__file_path'))

    def test_saving(self):
        """ Testing save method with new
        """
        meth = self._model.to_dict()
        _key = meth['__class__'] + "." + meth['id']
        storage = FileStorage()
        storage.save()
        with open("Aras.json", 'r') as f:
            file_ = json.load(f)
        new = file_[_key]
        for key in new:
            self.assertEqual(meth[key], new[key])


if __name__ == "__main__":
    unittest.main()
