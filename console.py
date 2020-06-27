#!/usr/bin/python3
import cmd
import sys
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    __functions = {
        "BaseModel"
    }

    def do_quit(self, s):
        return True

    def help_quit(self):
        print("Quit command to exit the program\n")

    def emptyline(self):
        pass

    do_EOF = do_quit
    help_EOF = help_quit

    def do_create(self, arg):
        args = parse(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__functions:
            print("** class doesn't exist")
        else:
            print(eval(args[0]().id))
            storage.save()

def parse(arg):
    return tuple(map(str, arg.split()))

if __name__ == '__main__':
    HBNBCommand().cmdloop()
