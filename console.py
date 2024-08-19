#!/usr/bin/python3
"""
This module contains the entry point for the command interpreter.
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """
    Command interpreter class for AirBnB clone.
    """
    prompt = "(hbnb) "

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
