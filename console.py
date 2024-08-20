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

    def default(self, line):
        """Handle <class name>.all() command."""
        args = line.split(".")
        if len(args) == 2:
            class_name = args[0]
            method_call = args[1].strip("()").split("(")
            command = method_call[0]
            id_param = method_call[1].strip("\"'") if len(
                    method_call) > 1 else None

            if class_name in self.classes:
                if command == "all":
                    self.do_all(class_name)
                elif command == "count":
                    self.do_count(class_name)
                elif command == "show" and id_param:
                    self.do_show(f"{class_name} {id_param}")
                elif command == "destroy" and id_param:
                    self.do_destroy(f"{class_name} {id_param}")
                else:
                    print(f"*** Unknown syntax: {line}")
            else:
                print(f"** class doesn't exist **")
        else:
            print(f"*** Unknown syntax: {line}")

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

    def do_all(self, class_name):
        """Retrieve all instances of a class."""
        all_objects = storsge.all()
        class_objects = [
                str(obj) for key, obj in all_objects.items()
                if key.startswith(f"{clss_name}.")
        ]
        print(class_objects)

    def do_count(self, class_name):
        """Retrieve the number of instances of a class."""
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        count = sum(1 for key in storage.all() if key.startswith(
            f"{class_name}."))
        print(count)

    def do_show(self, arg):
        """show an instane based on its class name and id."""
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

    def do_create(self, class_name):
        """
        Creates a new instance of a class and saves it to JSON file.
        """
        if not class_name:
            print("** class name missing **")
            return
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        new_instance = self.classes[class_name]()
        new_instance.save()
        print(new_instance.id)

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

    def do_all(self, class_name):
        """Prints all string representation of all instances based
        or not on the class name.
        """
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        all_objects = storage.all()
        class_objects = [
                str(obj) for key, obj in all_objects.items()
                if key.startswith(f"{class_name}.")
        ]
        print(class_objects)

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
