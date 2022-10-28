"""The console module"""
from models.base_model import BaseModel
import cmd


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb)"
    selected = ["user", "state"]

    def postloop(self):
        print("Thank you")

    def do_EOF(self, line):
        """This command is used to exit the program
        Usage: EOF
        """
        return True

    def do_quit(self, line):
        """This command is used to exit the program
        Usage: exit
        """
        return True

    def emptyline(self):
        """Do nothing when line is empty"""
        pass

    #Test function
    def do_greet(self, line):
        if line:
            line = line.split()
            print("welcome", line[1])
        else:
            print("welcome")

    """Creating the console commands"""
    def do_create(self, line):
        """This is the command to create new instances
        Usage: create <name>"""
        if not line:
            print("** class name missing **")
        elif line not in HBNBCommand.selected:
            print("** class doesn't exist **")
        else:
            line = BaseModel()
            print(line.id)

    def do_show(self, line):
        """Prints the string representation of an 
        instance based on the class name and id
        usage: show BaseModel 1234-1234-1234
        """
        if line:
            line = line.split()
            if len(line) == 1:
                print("** instance id missing **")
            elif len(line) == 2:
                name = line[0]
                name_id = line[1]
                if name not in type(self).selected:
                    print("** class doesn't exist **")




if __name__ == "__main__":
    HBNBCommand().cmdloop("Welcome to my console")
