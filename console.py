#!/usr/bin/env python3
"""Module for HBNB command interpreter"""

import cmd
import re
import models
from shlex import split
from models import storage


def parse(arg):
    """Look for curly braces and square_brackets match using re"""
    curly_brace_match = re.search(r"\{(.*?)\}", arg)
    square_brackets_match = re.search(r"\[(.*?)\]", arg)

    if curly_brace_match is None:
        if square_brackets_match is None:
            return [i.strip(",") for i in split(arg)]
        else:
            tokens = arg[:square_brackets_match.span()[0]].split()
            token = [token.strip(",") for token in tokens]
            token.append(square_brackets_match.group())
            return token
    else:
        tokens = arg[:curly_brace_match.span()[0]].split()
        token = [token.strip(",") for token in tokens]
        token.append(curly_brace_match.group())
        return token

class HBNBCommand(cmd.Cmd):
    """class for HBNB command interpreter"""

    prompt = "(hbnb) "

    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

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

    
    def do_show(self, arg):
        """Usage: show <class> <id> or <class>.show(<id>)
        Display the string representation of a class instance of a given id.
        """
        arglist = parse(arg)
        objdict = storage.all()
        if len(arglist) == 0:
            print("** class name missing **")
        elif arglist[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(arglist) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arglist[0], arglist[1]) not in objdict:
            print("** no instance found **")
        else:
            print(objdict["{}.{}".format(arglist[0], arglist[1])])

    def do_destroy(self, arg):
        """Usage: destroy <class> <id> or <class>.destroy(<id>)
        Delete a class instance of a given id.
        """
        arglist = arg.split()
        objdict = storage.all()
        if not arglist:
            print("** class name missing **")
        elif arglist[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")

        elif len(arglist) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arglist[0], arglist[1]) not in objdict.keys():
            print("** no instance found **")
        else:
            del objdict["{}.{}".format(arglist[0], arglist[1])]
            storage.save()

    def do_all(self, arg):
        """
            usage: all or all <class>
        prints all string representation of all instances based or not
        on the class name
        """
        arglist = arg.split()
        objdict = storage.all()
        instances_list = []
        if not arglist:
            for instance in objdict.values():
                instances_list.append(str(instance))
        elif arglist[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        else:
            for instance in objdict.values():
                if instance.__class__.__name__ == arglist[0]:
                    instances_list.append(str(instance))
        print(instances_list)

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
