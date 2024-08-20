#!/usr/bin/python3
"""
This module contains the entry point for the command interpreter.
"""

import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

# classes = {"BaseModel": BaseModel}


class HBNBCommand(cmd.Cmd):
    """
    Command interpreter class for AirBnB clone.
    """
    prompt = "(hbnb) "
    classes = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
            }

    def do_create(self, arg):
        """
        Creates a new instance of a class and saves it to JSON file.
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            obj = self.classes[args[0]]()
            obj.save()
            print(obj.id)

    def do_show(self, arg):
        """
        Prints the string representation of an instance based on the class
        name and id.
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = f"{args[0]}.{args[1]}"
            obj = storage.all().get(key)
            if obj:
                print(obj)
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id."""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = f"{args[0]}.{args[1]}"
            if key in storage.all():
                del storage.all()[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances based
        or not on the class name.
        """
        args = arg.split()
        if len(args) > 0 and args[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            objs = [str(obj) for key, obj in storage.all().items()
                    if len(args) == 0 or key.startswith(f"{args[0]}.")]
            print(objs)

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or
        updating attribute.
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            key = f"{args[0]}.{args[1]}"
            obj = storage.all().get(key)
            if obj:
                attr_name = args[2]
                attr_value = args[3].strip('"')
                if hasattr(obj, attr_name):
                    attr_type = type(getattr(obj, attr_name))
                    try:
                        setattr(obj, attr_name, attr_type(attr_value))
                    except valueError:
                        print("** invalid attribute value **")
                        obj.save()
                else:
                    print("** attribute name doesn't exist **")
            else:
                print("** no instance found **")

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program on EOF"""
        return True

    def emptyline(self):
        """Do nothing on an empty input line"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
