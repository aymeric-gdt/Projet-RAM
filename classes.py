import re

class RegistreManager:

    def __init__(self) -> None:
        self.content = dict()

    def add_registre(self, rX:str):
        self.content[rX] = 0
    
    def get_registre(self, rX:str)->int:
        if rX not in self.content:
            self.add_registre(rX)
        return self.content[rX]
    
    def set_registre(self, rX:str, value:int):
        if rX not in self.content:
            self.add_registre(rX)
        self.content[rX] = value


class MachineUniverselle:

    def __init__(self) -> None:
        self.registres = RegistreManager()
        self.tasks = []
        self.step = 0
    
    def __get_value(self, arg) -> int:
        if type(arg) is str:
            arg = arg.split("@")
            if len(arg)>1:
                arg = f"{arg[0]}{self.registres.get_registre(arg)}"
            else:
                arg = arg[0]
            arg = self.registres.get_registre(arg)
        return arg
            
    
    def __ADD(self, args):
        self.registres.set_registre(args[2], self.__get_value(args[0]) + self.__get_value(args[1]))
        return 1

    def __SUB(self, args):
        self.registres.set_registre(args[2], self.__get_value(args[0]) - self.__get_value(args[1]))
        return 1

    def __MULT(self, args):
        self.registres.set_registre(args[2], self.__get_value(args[0]) * self.__get_value(args[1]))
        return 1

    def __DIV(self, args):
        self.registres.set_registre(args[2], self.__get_value(args[0]) // self.__get_value(args[1]))
        return 1

    def __MOD(self, args):
        self.registres.set_registre(args[2], self.__get_value(args[0]) % self.__get_value(args[1]))
        return 1

    
    def build(self,path_of_ram_machine:str="test.ram"):
        """Build RAM Machine from .ram file"""
        command_finder = re.compile(r'[A-Z][A-Z]+')
        parenthese_finder = re.compile(r'\(|\)')
        integer_finder = re.compile(r'^[0-9]+$|^-[0-9]+$')

        with open(path_of_ram_machine,"r") as f:
            while (line:=f.readline()) != "":
                line = line.replace('\n','')
                x,y = command_finder.search(line).span()
                command = line[x:y] #########
                args = parenthese_finder.sub('',line[y:]).split(',')
                for i in range(len(args)):
                    if integer_finder.fullmatch(args[i]):
                        args[i] = int(args[i])
                task = (command, ...)
                self.tasks.append(task)