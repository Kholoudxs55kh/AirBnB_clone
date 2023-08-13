#!/usr/bin/python3
"""Console Test Cases
"""
import unittest
from unittest.mock import patch
from io import StringIO
import os
import json
import console
import tests
from console import HBNBCommand
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage


class TestConsole(unittest.TestCase):

    def tearDown(self):
        """Remove JSON file (Aras.json) after executing
        """
        try:
            os.remove("../Aras.json")
        except Exception:
            pass

    def test_docstrings(self):
        """Testing docstrings
        """
        self.assertIsNotNone(console.__doc__)
        self.assertIsNotNone(HBNBCommand().do_quit.__doc__)
        self.assertIsNotNone(HBNBCommand().do_EOF.__doc__)
        self.assertIsNotNone(HBNBCommand().emptyline.__doc__)
        self.assertIsNotNone(HBNBCommand().do_create.__doc__)
        self.assertIsNotNone(HBNBCommand().do_all.__doc__)
        self.assertIsNotNone(HBNBCommand().do_show.__doc__)
        self.assertIsNotNone(HBNBCommand().do_destroy.__doc__)
        self.assertIsNotNone(HBNBCommand().do_update.__doc__)
        self.assertIsNotNone(HBNBCommand().default.__doc__)

    def test_emptylines(self):
        """Testing Emptylines
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("\n")
        self.assertEqual(f.getvalue(), '')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("            \n")
        self.assertEqual(f.getvalue(), '')

    def test_spaces_in_command(self):
        """Testing Spaces, command is executed as normal
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("     help        create")
        self.assertEqual(f.getvalue(), 'Creates a New Instance\n        \n')

    def test_count(self):
        """Testing count
        """
        try:
            # to start counting from 0
            os.remove("Aras.json")
        except Exception:
            pass

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            HBNBCommand().onecmd("create BaseModel")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.count()")
        self.assertNotEqual(f.getvalue(), '1')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("id.count()")
        self.assertEqual(f.getvalue(), "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.count)")
        self.assertEqual(f.getvalue(), "** method doesn't exist **\n")

    def test_update(self):
        """Testing Update
        """
        try:
            os.remove("Aras.json")
        except Exception:
            pass

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
        id = f.getvalue()

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update")
        self.assertEqual(f.getvalue(), '** class name missing **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update asdasdas")
        self.assertEqual(f.getvalue(), "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update User")
        self.assertEqual(f.getvalue(), '** instance id missing **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update User " + id)
        self.assertEqual(f.getvalue(), '** attribute name missing **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update User " + id + " age ")
        self.assertEqual(f.getvalue(), '** value missing **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('Cukur.update("{}")'.format(id))
        self.assertEqual(f.getvalue(), "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.update()")
        self.assertEqual(f.getvalue(), '** instance id missing **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('User.update("{}", "age")'.format(id))
        self.assertEqual(f.getvalue(), '** no instance found **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('User.update("{}", "age")'.format(id))
        self.assertEqual(f.getvalue(), '** no instance found **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('User.update("{}", "age", "27")'.
                                 format(id))
        self.assertEqual(f.getvalue(), '** no instance found **\n')

    def test_help(self):
        """Testing help based on Docstring
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help quit")
        self.assertEqual(f.getvalue(), 'Quits The Program\n        \n')

    def test_create(self):
        """Testing create method
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Cumali")
        self.assertEqual(f.getvalue(), "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create")
        self.assertEqual(f.getvalue(), '** class name missing **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            # got some help here
        self.assertRegex(f.getvalue(), '^[0-9a-f]{8}-[0-9a-f]{4}-[1-5]'
                                       '[0-9a-f]{3}-[89ab][0-9a-f]{3}-'
                                       '[0-9a-f]{12}$')

    def test_EOF(self):
        """Testing EOF
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("EOF")
        self.assertEqual(f.getvalue(), '\n')

    def test_show(self):
        """Testing show
        """
        try:
            os.remove("Aras.json")
        except Exception:
            pass

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show")
        self.assertEqual(f.getvalue(), '** class name missing **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show Yamac")
        self.assertEqual(f.getvalue(), "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show User")
        self.assertEqual(f.getvalue(), '** instance id missing **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show User 556271")
        self.assertEqual(f.getvalue(), '** no instance found **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.show(54263)")
        self.assertEqual(f.getvalue(), '** no instance found **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Cukur.show(1)")
        self.assertEqual(f.getvalue(), "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.show()")
        self.assertEqual(f.getvalue(), '** instance id missing **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.show)")
        self.assertEqual(f.getvalue(), "** method doesn't exist **\n")

    def test_destroy(self):
        """Testing destroy
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy")
        self.assertEqual(f.getvalue(), '** class name missing **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy Yucil")
        self.assertEqual(f.getvalue(), "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy User")
        self.assertEqual(f.getvalue(), '** instance id missing **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy User 111")
        self.assertEqual(f.getvalue(), '** no instance found **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.destroy(132736)")
        self.assertEqual(f.getvalue(), '** no instance found **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Cukur.destroy('asqq12342')")
        self.assertEqual(f.getvalue(), "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.destroy()")
        self.assertEqual(f.getvalue(), '** instance id missing **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.destroy)")
        self.assertEqual(f.getvalue(), "** method doesn't exist **\n")

    def test_wrong_command(self):
        """No action should execute
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Cukur")
        self.assertEqual(f.getvalue(), '')

    def test_all(self):
        """Testing all
        """
        try:
            os.remove("Aras.json")
        except Exception:
            pass
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all")
        self.assertNotEqual(f.getvalue(), '')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all BaseModel")
        self.assertNotEqual(f.getvalue(), '')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all Cukur")
        self.assertEqual(f.getvalue(), "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.all()")
        self.assertNotEqual(f.getvalue(), '')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Cukur.all()")
        self.assertEqual(f.getvalue(), "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.all)")
        self.assertEqual(f.getvalue(), "** method doesn't exist **\n")


if __name__ == '__main__':
    unittest.main()
