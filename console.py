#!/usr/bin/env python3
"""Module for HBNB command interpreter"""

import cmd

class HBNBCommand(cmd.Cmd):
    """class for HBNB command interpreter"""

    prompt = "(hbnb) "

    def do_create(self, arg):

        """Creates a new instance of BaseModel"""
        if not arg:
            print("** class name missing **")
            return
        try:
            cls = eval(arg)
            obj = cls()
            obj.save()
            print(obj.id)
        except NameError:
            print("** class doesn't exist **")

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

if __name__ == "__main__":
    HBNBCommand().cmdloop()
