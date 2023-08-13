#!/usr/bin/python3
""" Unit test amenity """


import unittest
import models
import os
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """ Test for class amenity"""

    def testin_executable_file(self):
        '''test if file has permissions u+x to execute'''
        # Check for read access
        is_read_true = os.access('models/amenity.py', os.R_OK)
        self.assertTrue(is_read_true)
        # Check for write access
        is_write_true = os.access('models/amenity.py', os.W_OK)
        self.assertTrue(is_write_true)
        # Check for execution access
        is_exec_true = os.access('models/amenity.py', os.X_OK)
        self.assertTrue(is_exec_true)

    def test_init_amenity(self):
        """tssting the Amentiy (obj)"""
        my_object = Amenity()
        self.assertIsInstance(my_object, Amenity)

    def testing_id(self):
        """ testing that id is unique """
        my_objectId0 = Amenity()
        my_objectId1 = Amenity()
        self.assertNotEqual(my_objectId0.id, my_objectId1.id)

    def testing_str(self):
        '''checking the str format'''
        my_strobject = Amenity()
        dictt = my_strobject.__dict__
        string0 = "[Amenity] ({}) {}".format(my_strobject.id, dictt)
        string1 = str(my_strobject)
        self.assertEqual(string0, string1)

    def testing_save(self):
        """ check if date update when save """
        object_upd = Amenity()
        first_update = object_upd.updated_at
        object_upd.save()
        second_update = object_upd.updated_at
        self.assertNotEqual(first_update, second_update)

    def test_to_dict(self):
        '''checking id to dict returns a dic with
        class Amenity, with iso string convertion.'''
        my_modell = Amenity()
        my_dict_modell = my_modell.to_dict()
        self.assertIsInstance(my_dict_modell, dict)
        for key, value in my_dict_modell.items():
            flag = 0
            if my_dict_modell['__class__'] == 'Amenity':
                flag += 1
            self.assertTrue(flag == 1)
        for key, value in my_dict_modell.items():
            if key == 'created_at':
                self.assertIsInstance(value, str)
            if key == 'updated_at':
                self.assertIsInstance(value, str)


if __name__ == '__main__':
    unittest.main()
