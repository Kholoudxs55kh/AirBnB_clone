#!/usr/bin/python3
"""a program called console.py that contains the
entry point of the command interpreter"""
import cmd
from models.base_model import BaseModel
import models


class HBNBCommand(cmd.Cmd):
    """Class Constructor"""

    prompt = '(hbnb) '
    Classes_Name = ['BaseModel']

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

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
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
            del (all_[id_])
            models.storage.save()
        else:
            print('** no instance found **')

    def do_all(self, line):
        """Prints all string representation of all instances"""
        all_ = models.storage.all()
        # args = line.split(" ")
        if not line:
            for value in all_.values():
                print([str(value)])
        elif line:
            if line in self.Classes_Name:
                for value in all_.values():
                    if value.__class__.__name__ == line:
                        print([str(value)])
            else:
                print("** class doesn't exist **")

    def do_update(self):
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()