#!/usr/bin/python3
""" Unit test Review """
import unittest
import models
import os
from models.review import Review


class TestReview(unittest.TestCase):
    """ Test for class Review"""

    def testing_executable_file(self):
        '''test if file's permissions'''
        # Check for read access
        read_true = os.access('models/review.py', os.R_OK)
        self.assertTrue(read_true)
        # Check for write access
        write_true = os.access('models/review.py', os.W_OK)
        self.assertTrue(write_true)
        # Check for execution access
        exec_true = os.access('models/review.py', os.X_OK)
        self.assertTrue(exec_true)

    def testing_init_Review(self):
        """test if an object is an type Review"""
        my_object = Review()
        self.assertIsInstance(my_object, Review)

    def testing_id(self):
        """ test that id is unique """
        my_objectId = Review()
        my_objectId1 = Review()
        self.assertNotEqual(my_objectId.id, my_objectId1.id)

    def test_str(self):
        '''check str format'''
        my_strobject = Review()
        dictt = my_strobject.__dict__
        string0 = "[Review] ({}) {}".format(my_strobject.id, dictt)
        string1 = str(my_strobject)
        self.assertEqual(string0, string1)

    def testing_save(self):
        """ check if date tpdate when save """
        object_upd = Review()
        first_update = object_upd.updated_at
        object_upd.save()
        second_update = object_upd.updated_at
        self.assertNotEqual(first_update, second_update)

    def testing_to_dict(self):
        '''check if to_dict returns a dictionary,with
        class Review, with iso format'''
        my_modell = Review()
        my_dict_modell = my_modell.to_dict()
        self.assertIsInstance(my_dict_modell, dict)
        for key, value in my_dict_modell.items():
            flag = 0
            if my_dict_modell['__class__'] == 'Review':
                flag += 1
            self.assertTrue(flag == 1)
        for key, value in my_dict_modell.items():
            if key == 'created_at':
                self.assertIsInstance(value, str)
            if key == 'updated_at':
                self.assertIsInstance(value, str)


if __name__ == '__main__':
    unittest.main()
