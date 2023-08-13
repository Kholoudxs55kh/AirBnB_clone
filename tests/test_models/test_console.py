#!/usr/bin/python3
"""
Unit tests for console using Mock module from py stanred lib
"""

import os
import sys
import unittest
from unittest.mock import create_autospec, patch
from io import StringIO
from console import HBNBCommand
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class TestConsole(unittest.TestCase):
    """
    Unittest for the console model
    """

    def setUp(self):
        """stdin& stdout redirection"""
        self.mock_stdin = create_autospec(sys.stdin)
        self.mock_stdout = create_autospec(sys.stdout)
        self.err = ["** class name missing **",
                    "** class doesn't exist **",
                    "** instance id missing **",
                    "** no instance found **",
                    ]

        self.cls = ["BaseModel",
                    "User",
                    "State",
                    "City",
                    "Place",
                    "Amenity",
                    "Review"]

    def create(self, server=None):
        """
        Redirection to the mock module
        """
        return HBNBCommand(stdin=self.mock_stdin, stdout=self.mock_stdout)

    def last_write(self, nrr=None):
        """Returns last n output"""
        if nrr is None:
            return self.mock_stdout.write.call_args[0][0]
        return "".join(map(lambda c: c[0][0],
                           self.mock_stdout.write.call_args_list[-nrr:]))

    def test_quit(self):
        """Quit command"""
        cl = self.create()
        self.assertTrue(cl.onecmd("quit"))


if __name__ == '__main__':
    unittest.main()
