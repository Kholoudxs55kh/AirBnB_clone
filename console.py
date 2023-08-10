#!/usr/bin/python3
"""a program called console.py that contains the
entry point of the command interpreter"""
import cmd
from models.base_model import BaseModel
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import models


class HBNBCommand(cmd.Cmd):
    """Class Constructor"""

    prompt = '(hbnb) '
    Classes_Name = ['BaseModel', 'User', 'City', 'State'
                   'Amenity', 'Place', 'Review']

    def do_quit(self, line):
        """Quits The Program
        """
        exit()

    def do_EOF(self, line):
        """Exits The Program
        """
        print()
        return True

    def emptyline(self):
        """Passes The EmptyLines"""
        return super().emptyline()

    def do_create(self, line):
        """Creates a New Instance"""
        if len(line) == 0:
            print("** class name missing **")
            return

        args = line.split(" ")

        try:
            if args[0] not in self.Classes_Name:
                print("** class doesn't exist **")
        except NameError:
            pass
        # now in the 1st arg we have the Class Name,
        # to make it functionable we should use eval()
        className = eval(args[0])()
        className.save()

        print(className.id)

    def do_show(self, line):
        """Prints the string representation of an instance"""
        if len(line) == 0:
            print("** class name missing **")
            return
        args = line.split(" ")

        try:
            if args[0] not in self.Classes_Name:
                print("** class doesn't exist **")
        except NameError:
            pass

        if len(line) == 1:
            print("** instance id missing **")

        all_ = models.storage.all()

        id_ = args[0] + "." + args[1]
        if id_ in all_:
            print(all_[id_])
        else:
            print('** no instance found **')

    def do_destroy(self):
        pass

    def do_all(self):
        pass

    def do_update(self):
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
