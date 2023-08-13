#!/usr/bin/python3
""" Unit test Review """
from sre_parse import State
import unittest
import models
import os
from models.user import User


class TestUser(unittest.TestCase):
    """ Test for class user"""

    def testing_executable_file(self):
        '''test if file's permissions'''
        # Check for read access
        read_true = os.access('models/user.py', os.R_OK)
        self.assertTrue(read_true)
        # Check for write access
        write_true = os.access('models/user.py', os.W_OK)
        self.assertTrue(write_true)
        # Check for execution access
        exec_true = os.access('models/user.py', os.X_OK)
        self.assertTrue(exec_true)

    def testing_init_Review(self):
        """test if an object is an type Review"""
        my_object = User()
        self.assertIsInstance(my_object, User)

    def testing_id(self):
        """ test that id is unique """
        my_objectId = User()
        my_objectId1 = User()
        self.assertNotEqual(my_objectId.id, my_objectId1.id)

    def test_str(self):
        '''check str format'''
        my_strobject = User()
        dictt = my_strobject.__dict__
        string0 = "[User] ({}) {}".format(my_strobject.id, dictt)
        string1 = str(my_strobject)
        self.assertEqual(string0, string1)

    def testing_save(self):
        """ check if date tpdate when save """
        object_upd = User()
        first_update = object_upd.updated_at
        object_upd.save()
        second_update = object_upd.updated_at
        self.assertNotEqual(first_update, second_update)

    def testing_to_dict(self):
        '''check if to_dict returns a dictionary,with
        class Review, with iso format'''
        my_modell = User()
        my_dict_modell = my_modell.to_dict()
        self.assertIsInstance(my_dict_modell, dict)
        for key, value in my_dict_modell.items():
            flag = 0
            if my_dict_modell['__class__'] == 'User':
                flag += 1
            self.assertTrue(flag == 1)
        for key, value in my_dict_modell.items():
            if key == 'created_at':
                self.assertIsInstance(value, str)
            if key == 'updated_at':
                self.assertIsInstance(value, str)


if __name__ == '__main__':
    unittest.main()
