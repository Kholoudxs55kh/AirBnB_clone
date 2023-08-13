#!/usr/bin/python3
""" Unit test City """

import unittest
import models
import os
from models.city import City


class TestCity(unittest.TestCase):
    """ Test for class city"""

    def testing_executable_file(self):
        '''test if files permission'''
        # Check for read access
        read_true = os.access('models/city.py', os.R_OK)
        self.assertTrue(read_true)
        # Check for write access
        write_true = os.access('models/city.py', os.W_OK)
        self.assertTrue(write_true)
        # Check for execution access
        exec_true = os.access('models/city.py', os.X_OK)
        self.assertTrue(exec_true)

    def testing_init_city(self):
        """test oobject's type"""
        my_object = City()
        self.assertIsInstance(my_object, City)

    def testing_id(self):
        """ test that id is unique """
        my_objectId0 = City()
        my_objectId1 = City()
        self.assertNotEqual(my_objectId0.id, my_objectId1.id)

    def testing_str(self):
        '''check str format'''
        my_strobject = City()
        dictt = my_strobject.__dict__
        string0 = "[City] ({}) {}".format(my_strobject.id, dictt)
        string1 = str(my_strobject)
        self.assertEqual(string0, string1)

    def testing_save(self):
        """ check if date update when save """
        object_upd = City()
        first_update = object_upd.updated_at
        object_upd.save()
        second_update = object_upd.updated_at
        self.assertNotEqual(first_update, second_update)

    def testing_to_dict(self):
        '''check if to_dict returns a dictionary,
        class name : city , with iso format'''
        my_model3 = City()
        my_dict_modell = my_model3.to_dict()
        self.assertIsInstance(my_dict_modell, dict)
        for key, value in my_dict_modell.items():
            flag = 0
            if my_dict_modell['__class__'] == 'City':
                flag += 1
            self.assertTrue(flag == 1)
        for key, value in my_dict_modell.items():
            if key == 'created_at':
                self.assertIsInstance(value, str)
            if key == 'updated_at':
                self.assertIsInstance(value, str)


if __name__ == '__main__':
    unittest.main()
