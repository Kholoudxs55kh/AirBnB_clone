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
    Methods = ["all", "count", "show", "update", "destroy", "create"]

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
                return
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
                return
        except NameError:
            pass

        if len(args) == 1:
            print("** instance id missing **")
            return

        all_ = models.storage.all()

        id_ = args[0] + "." + args[1]
        if id_ in all_:
            print(all_[id_])
        else:
            print('** no instance found **')
            return

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        if len(line) == 0:
            print("** class name missing **")
            return
        args = line.split(" ")

        try:
            if args[0] not in self.Classes_Name:
                print("** class doesn't exist **")
                return
        except NameError:
            pass

        if len(args) == 1:
            print("** instance id missing **")
            return

        all_ = models.storage.all()
        id_ = args[0] + "." + args[1]
        if id_ in all_:
            del (all_[id_])
            models.storage.save()
        else:
            print('** no instance found **')
            return

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
                return

    def do_update(self, line):
        """Updates an Attribute"""
        if len(line) == 0:
            print("** class name missing **")
            return
        args = line.split(" ")

        try:
            if args[0] not in self.Classes_Name:
                print("** class doesn't exist **")
                return
        except NameError:
            pass

        if len(args) == 1:
            print("** instance id missing **")
            return

        all_ = models.storage.all()
        id_ = args[0] + "." + args[1]
        if id_ in all_:
            if args[3][0] in ("'", '"') and args[3][-1] in ("'", '"'):
                setattr(all_[id_], args[2], args[3][1:-1])
            else:
                setattr(all_[id_], args[2], args[3])
            all_[id_].save()
        else:
            print('** no instance found **')
            return

        if len(args) == 2:
            print("** attribute name missing **")
            return

        if len(args) == 3:
            print("** value missing **")
            return

        if len(args) > 4:
            pass

# User.show("246c227a-d5c1-403d-9bc7-6a47bb9f0f68")
    def default(self, line):
        if "." in line or "(" in line or "," in line:
            all_ = models.storage.all()
            class_ = line[: line.index(".")]
            method_ = line[line.index(".") + 1: line.index("(")]
            # if line[line.index("(") + 1] == ")":
            # idd = line[line.index("(") + 1: line.index(")")]
            # method_ = line[line.index(".") + 1: line.index("(")]

            if line[line.index("(") + 1] != ")":
                # class_ = line[: line.index(".")]
                # method_ = line[line.index(".") + 1: line.index("(")]()
                l_i = line.index("(")
                if " " in line[l_i + 1:] or "," in line[l_i + 1:]:
                    args = line[line.index("(") + 1: -1].split(", ")
        # User.update("id", {'first_name': "John", "age": 89})
                    # if len(args) == 3:
                    #     _id = args[0][1:-1]
                    #     _attName = args[1]
                    #     _attValue = args[2]
                    # elif len(args) == 2:
                    #     _id = args[0][1:-1]
                    #     if args[1].startswith("{"):
                    #         _dict = args[1]
                else:
                    _id = line[line.index("(") + 2: line.index(")") - 1]

            if class_ in self.Classes_Name and method_ in self.Methods:
                if method_ == "all":
                    for value in all_.values():
                        if value.__class__.__name__ == class_:
                            print([str(value)])
                    return

                elif method_ == "count":
                    count = 0
                    for value in all_.values():
                        if value.__class__.__name__ == class_:
                            count += 1
                    print(int(count))
                    return
            # User.show("246c227a-d5c1-403d-9bc7-6a47bb9f0f68")
                elif method_ == "show":
                    id_ = class_ + "." + _id
                    # print("Show!")
                    if id_ in all_:
                        print(all_[id_])
                        # print("Show!")
                        return
                    else:
                        print('** no instance found **')
                        return
                elif method_ == "destroy":
                    id_ = class_ + "." + _id
                    if id_ in all_:
                        del (all_[id_])
                        models.storage.save()
                        return
                    else:
                        print('** no instance found **')
                        return
                elif method_ == "update":
                    _dict = {}
                    # id_ = class_ + "." + _id
                    if len(args) == 3:
                        _id = args[0][1:-1]
                        _attName = args[1]
                        _attValue = args[2]
                    elif len(args) == 2:
                        _id = args[0][1:-1]
                        if args[1].startswith("{"):
                            for key, value in args[1]:
                                _dict[key] = value
# User.update("id", {'first_name': "John", "age": 89})
                    id_ = class_ + "." + _id
                    if len(args) == 0:
                        print("** instance id missing **")
                        return
                    if len(args) == 1:
                        print("** attribute name missing **")
                        return
                    tt = ('"', "'")
                    if id_ in all_:
                        if len(args) == 2:
                            if type(_dict) == dict:
                                for key, value in _dict.items():
                                    if key[0] in tt and value[0] in tt:
                                        setattr(all_[id_],
                                                key[1:-1], value[1:-1])
                                    elif key[0] in ('"', "'"):
                                        setattr(all_[id_], key[1:-1], value)
                                    elif value[0] in ('"', "'"):
                                        setattr(all_[id_], key, value[1:-1])
                                    else:
                                        setattr(all_[id_], key, value)
                                    all_[id_].save()
                                return
                            else:
                                print("** value missing **")
                                return
                        elif len(args) == 3:
                            if _attName[0] in tt and _attValue[0] in tt:
                                setattr(all_[id_],
                                        _attName[1:-1], _attValue[1:-1])
                            elif _attName[0] in ('"', "'"):
                                if _attName in ("id", "updated_at",
                                                "created_at"):
                                    pass
                                else:
                                    setattr(all_[id_],
                                            _attName[1:-1], _attValue)
                            elif _attValue[0] in ('"', "'"):
                                setattr(all_[id_], _attName, _attValue[1:-1])
                            else:
                                setattr(all_[id_], _attName, _attValue)
                            all_[id_].save()
                        return
                    else:
                        print('** no instance found **')
                        return
            else:
                print("** class doesn't exist **")
                return
        else:
            pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
