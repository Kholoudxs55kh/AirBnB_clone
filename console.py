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
    Classes_Name = ['BaseModel', 'User', 'City', 'State',
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
        """Passes The EmptyLines
        """
        pass

    def do_create(self, line):
        """Creates a New Instance
        """
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
        """Prints the string representation of an instance
        """
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
        """Deletes an instance based on the class name and id
        """
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
        """Prints all string representation of all instances
        """
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
        """Updates an Attribute
        """
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
        if len(args) == 2:
            print("** attribute name missing **")
            return

        if len(args) == 3:
            print("** value missing **")
            return

        all_ = models.storage.all()
        id_ = args[0] + "." + args[1]
        if id_ in all_:
            if args[3][0] in ("'", '"') and args[3][-1] in ("'", '"'):
                try:
                    value = int(args[3][1:-1])
                except ValueError:
                    try:
                        value = float(args[3][1:-1])
                    except ValueError:
                        if " " in args[3]:
                            value = args[3]
                        value = args[3][1:-1]

                setattr(all_[id_], args[2], value)

            all_[id_].save()
        else:
            print('** no instance found **')
            return

        if len(args) > 4:
            pass

# User.show("246c227a-d5c1-403d-9bc7-6a47bb9f0f68")
    def default(self, line):
        """ default commands
        """
        if "." in line or "(" in line or "," in line:
            all_ = models.storage.all()
            class_ = line[: line.index(".")]
            m = ("show", "update", "destroy")
            if line[-1] == ")" and "(" in line:
                method_ = line[line.index(".") + 1: line.index("(")]
                if method_ in m and line[-2:] == "()":
                    print("** instance id missing **")
                    return
            else:
                print("** method doesn't exist **")
                return
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
                    if len(args) == 3:
                        _id = args[0][1:-1]
                        _attName = args[1]
                        _attValue = args[2]
                    elif len(args) == 2:
                        _id = args[0][1:-1]
                        if args[1].startswith("{"):
                            _dict = args[1]
                else:
                    _id = line[line.index("(") + 2: line.index(")") - 1]

            if class_ in self.Classes_Name:
                if method_ in self.Methods or method_[-2:] != "()":
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
                        if not _id:
                            print("** instance id missing **")
                            return
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
                        if not _id:
                            print("** instance id missing **")
                            return
                        id_ = class_ + "." + _id
                        if id_ in all_:
                            del (all_[id_])
                            models.storage.save()
                            return
                        else:
                            print('** no instance found **')
                            return
# ================================================================
# ================================================================
# ================================================================
                    elif method_ == "update":
                        _dict = {}
                        if len(args) == 3:
                            _id = args[0][1:-1]
                            if not _id:
                                print("** instance id missing **")
                                return
                            _attName = args[1]
                            _attValue = args[2]
                        elif len(args) == 2:
                            _id = args[0][1:-1]
                        if len(args) == 1:
                            print("** attribute name missing **")
                            return
                        id_ = class_ + "." + _id
                        t = ('"', "'")
                        if id_ in all_:
                            if len(args) == 2:
                                _id = args[0][1:-1]
                                if args[1].startswith("{"):
                                    arg_ = args[1][1:-1]
                                    arg = arg_.split(", ")
                                    for i in arg:
                                        _key = i[:i.index(":")].strip()
                                        _value = i[i.index(":") + 1:].strip()
                                        _dict[_key] = _value
                                    for key, value in _dict.items():
                                        if value[0] in t and value[-1] in t:
                                            if key[0] in t and key[-1] in t:
                                                setattr(all_[id_],
                                                        eval(key), value[1:-1])
                                            setattr(all_[id_],
                                                    key, value[1:-1])
                                        else:
                                            if key[0] in t and key[-1] in t:
                                                setattr(all_[id_],
                                                        eval(key), eval(value))
                                            setattr(all_[id_],
                                                    key, eval(value))
                                        all_[id_].save()
                                    return
                                else:
                                    print("** value missing **")
                                    return
                            elif len(args) == 3:
                                _id = args[0][1:-1]
                                if not _id:
                                    print("** instance id missing **")
                                    return
                                _attName = args[1].strip()
                                _attValue = args[2].strip()
                                if _attValue[0] in t and _attValue[-1] in t:
                                    if _attName[0] in t and _attName[-1] in t:
                                        setattr(all_[id_],
                                                _attName[1:-1],
                                                _attValue[1:-1])
                                    setattr(all_[id_],
                                            _attName, _attValue[1:-1])
                                else:
                                    if _attName[0] in t and _attName[-1] in t:
                                        setattr(all_[id_],
                                                _attName[1:-1],
                                                eval(_attValue))
                                    _attValue = _attValue.strip()
                                    setattr(all_[id_],
                                            _attName, eval(_attValue))
                                all_[id_].save()
                            return
                        else:
                            print('** no instance found **')
                            return
                else:
                    print("** method doesn't exist **")
                    return
            else:
                print("** class doesn't exist **")
                return
        else:
            pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
