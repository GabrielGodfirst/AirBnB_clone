#!/usr/bin/python3

"""Console module for HBNB project."""

import cmd


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class for the command-line interpreter.

    Attributes:
        prompt (str): The prompt displayed to the user.
    """

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print("")
        return True

    def emptyline(self):
        """Do nothing on empty line"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
