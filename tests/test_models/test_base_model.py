#!/usr/bin/python3
""" Unit test BaseModel """

import unittest
import models
import os
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """ Test for class BaseModel"""

    def testing_executable_file(self):
        '''testing the permissions'''
        # Check for read access
        read_true = os.access('models/base_model.py', os.R_OK)
        self.assertTrue(read_true)
        # Check for write access
        write_true = os.access('models/base_model.py', os.W_OK)
        self.assertTrue(write_true)
        # Check for execution access
        exec_true = os.access('models/base_model.py', os.X_OK)
        self.assertTrue(exec_true)

    def testing_init_BaseModel(self):
        """tesstinn the type of the obj"""
        my_object = BaseModel()
        self.assertIsInstance(my_object, BaseModel)

    def testing_id(self):
        """ test that id is unique """
        my_objectId0 = BaseModel()
        my_objectId1 = BaseModel()
        self.assertNotEqual(my_objectId0.id, my_objectId1.id)

    def testing_magic_str(self):
        '''check the  str format'''
        my_strobject = BaseModel()
        dictt = my_strobject.__dict__
        string0 = "[BaseModel] ({}) {}".format(my_strobject.id, dictt)
        string1 = str(my_strobject)
        self.assertEqual(string0, string1)

    def testing_save(self):
        """ check if date update when save """
        is_updated = BaseModel()
        first = is_updated.updated_at
        is_updated.save()
        second = is_updated.updated_at
        self.assertNotEqual(first, second)

    def testing_to_dict(self):
        '''checking if the new dict has exists , 
        has the iso convertion , returs value'''
        my_modell = BaseModel()
        my_dict_modell = my_modell.to_dict()
        self.assertIsInstance(my_dict_modell, dict)
        for key, value in my_dict_modell.items():
            flag = 0
            if my_dict_modell['__class__'] == 'BaseModel':
                flag += 1
            self.assertTrue(flag == 1)
        for key, value in my_dict_modell.items():
            if key == 'created_at':
                self.assertIsInstance(value, str)
            if key == 'updated_at':
                self.assertIsInstance(value, str)


if __name__ == '__main__':
    unittest.main()
