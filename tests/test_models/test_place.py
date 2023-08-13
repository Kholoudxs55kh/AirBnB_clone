#!/usr/bin/python3
""" Unit test Place """
import unittest
import models
import os
from models.place import Place


class TestPlace(unittest.TestCase):
    """ Test for class Place"""

    def testing_executable_file(self):
        '''test files's permisssion'''
        # Check for read access
        read_true = os.access('models/place.py', os.R_OK)
        self.assertTrue(read_true)
        # Check for write access
        write_true = os.access('models/place.py', os.W_OK)
        self.assertTrue(write_true)
        # Check for execution access
        exec_true = os.access('models/place.py', os.X_OK)
        self.assertTrue(exec_true)

    def testing_init_Place(self):
        """test if an object is an type Place"""
        my_object = Place()
        self.assertIsInstance(my_object, Place)

    def testing_id(self):
        """ test that id is unique """
        my_objectId0 = Place()
        my_objectId1 = Place()
        self.assertNotEqual(my_objectId0.id, my_objectId1.id)

    def testing_str(self):
        '''check str format'''
        my_strobject = Place()
        dictt = my_strobject.__dict__
        string0 = "[Place] ({}) {}".format(my_strobject.id, dictt)
        string1 = str(my_strobject)
        self.assertEqual(string0, string1)

    def testing_save(self):
        """ check if date update when save """
        object_upd = Place()
        first_update = object_upd.updated_at
        object_upd.save()
        second_update = object_upd.updated_at
        self.assertNotEqual(first_update, second_update)

    def testing_to_dict(self):
        '''check if dic format returs a dict with class place, iso format.'''
        my_modell = Place()
        my_dict_modell = my_modell.to_dict()
        self.assertIsInstance(my_dict_modell, dict)
        for key, value in my_dict_modell.items():
            flag = 0
            if my_dict_modell['__class__'] == 'Place':
                flag += 1
            self.assertTrue(flag == 1)
        for key, value in my_dict_modell.items():
            if key == 'created_at':
                self.assertIsInstance(value, str)
            if key == 'updated_at':
                self.assertIsInstance(value, str)


if __name__ == '__main__':
    unittest.main()
