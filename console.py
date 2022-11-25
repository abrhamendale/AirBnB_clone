#!/usr/bin/python3
"""Console module."""
import cmd
from models.__init__ import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review
c = ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]


class HBNBCommand(cmd.Cmd):
    """Console class"""
    intro = "Welcome to cmd\n"
    prompt = '(HBNB)'
    file = None

    def do_EOF(self, line):
        """EOF command to exit the program\n"""
        print()
        return True

    def do_quit(self, line):
        """Quit command to exit the program\n"""
        return True

    def do_create(self, line):
        """Creates class instance\n"""
        if (line):
            #if (line == "BaseModel"):
            try:
                model = eval(line)()#BaseModel()
                print(line)
                model.save()
                print(model.id)
            except Exception:
                print("class does not exist.")
                pass
                # return model.id
        else:
            print("class name missing")

    def do_show(self, line):
        """Prints class instance.\n"""
        #a,b = [s for s in line.split()]
        a = []
        for s in line.split():
            a.append(s)
        #print(storage.__objects) --- Needs setters and getters
        if len(a) > 0:
            if a[0] in c:
                if len(a) > 1:
                    i = a[0] + "." + a[1]
                    if i in (storage.objects).keys():
                        print("[{}] ({}) {}".format(a[0], i, storage.objects[i]))
                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_destroy(self, line):
        """Destroys instances.\n"""
        #a,b = [s for s in line.split()]
        a = []
        for s in line.split():
            a.append(s)
        #print(storage.__objects) --- Needs setters and getters
        if len(a) > 0:
            if a[0] in c:
                if len(a) > 1:
                    i = a[0] + "." + a[1]
                    if i in (storage.objects).keys():
                        del storage.objects[i]
                        storage.save()
                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_update(self, line):
        """Destroys instances.\n"""
        #a,b = [s for s in line.split()]
        a = []
        for s in line.split():
            a.append(s)#print(storage.__objects) --- Needs setters and getters
        print(a)
        if len(a) > 0:
            if a[0] in c:
                if len(a) > 1:
                    i = a[0] + "." + a[1]
                    if i in (storage.objects).keys():
                        if len(a) > 2:
                            if len(a) > 3:
                                storage.objects[i][a[2]] = a[3]
                                storage.save()
                            else:
                                print("** value missing **")
                        else:
                            print("** attribute name missing **")
                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_all(self, line):
        """Prints all instances.\n"""
        a = []
        if line in c:
            for key in storage.objects.keys():
                if line == key.split(".")[0]:
                    a.append(f"[{line}] ({(storage.objects[key])['id']}) {storage.objects[key]}")
        else:
            for key in storage.objects.keys():
                a.append(f"[{storage.objects[key]['__class__']}] ({(storage.objects[key])['id']}) {storage.objects[key]}")
        print(a)
        a = []

    def do_count(self, line):
        """Prints all instances.\n"""
        a = []
        if line in c:
            for key in storage.objects.keys():
                if line == key.split(".")[0]:
                    a.append(f"[{line}] ({(storage.objects[key])['id']}) {storage.objects[key]}")
        else:
            for key in storage.objects.keys():
                a.append(f"[{storage.objects[key]['__class__']}] ({(storage.objects[key])['id']}) {storage.objects[key]}")
        l = len(a)
        a = []
        return (l)

    def default(self, line):
        """Prints User instances"""
        print(line)
        a = []
        for s in line.split("."):
            a.append(s)
        if a[0] in c:
            if len(a) > 1:
                if a[1] == "all()":
                    self.do_all(a[0]);
                elif a[1] == "count()":
                    print(self.do_count(a[0]));
                cl = a[1].split("(\"")
                if cl[0] == "show":
                    self.do_show(a[0] + " " + cl[1].split("\")")[0])
                elif cl[0] == "destroy":
                    self.do_destroy(a[0] + " " + cl[1].split("\")")[0])



    #def do_EOF
if __name__ == '__main__':
    HBNBCommand().cmdloop()
