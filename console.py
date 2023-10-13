#!/usr/bin/python3
"""contains the entry point of the command interpreter"""
import cmd
import sys
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import json


class HBNBCommand(cmd.Cmd):
    """contains the entry point of the command interpreter"""
    prompt = '(hbnb) '

    def do_quit(self, line):
        """Quit command to exit the program"""
        sys.exit()

    def help_quit(self):
        print("Quit command to exit the program\n")

    def do_EOF(self, line):
        """handle program exit"""
        return True

    def emptyline(self):
        """handle emptyline"""
        pass

    def do_create(self, class_name):
        """Creates a new instance of BaseModel, saves it"""
        if not class_name:
            print("** class name missing **")
        elif class_name != 'BaseModel':
            print("** class doesn't exist **")
        else:
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, line):
        """Prints the string representation of an instance
        based on the class name and id"""
        args = line.split(' ')
        if not args[0]:
            print("** class name missing **")
        elif args[0] != 'BaseModel':
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            storage = FileStorage()
            storage.reload()
            data = storage.all()
            for key, value in data.items():
                _, obj_id = key.split('.')
                if obj_id == args[1]:
                    print(value)
                    return
            print("** no instance found **")

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        args = line.split(' ')
        if not args[0]:
            print("** class name missing **")
        elif args[0] != 'BaseModel':
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            storage = FileStorage()
            storage.reload()
            data = storage.all()
            found_key = False
            for key, value in data.items():
                _, obj_id = key.split('.')
                if obj_id == args[1]:
                    key_to_delete = key
                    found_key = True
                    break
            if found_key:
                del data[key_to_delete]
                obj = {k: v.to_dict() for k, v in data.items()}
                self.save_to_file(obj)
            else:
                print("** no instance found **")

    def save_to_file(self, dict_data):
        """save to json file"""
        file_path = 'file.json'
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(json.dumps(dict_data))



if __name__ == '__main__':
    HBNBCommand().cmdloop()
