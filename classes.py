import re

class RegistreManager:

    def __init__(self) -> None:
        self.input = []
        self.main = []
        self.output = []

    def add_registre(self, r:str):
        match r:
            case 'I':
                self.input.append(0)
            case 'R':
                self.main.append(0)
            case 'O':
                self.output.append(0)
    
    def get_registre(self, rX:str)->int:
        args = rX.split("@")

        match len(args):
            case 2:
                r,  = args[0]
            case 1:
                pass

        match rX:
            case 'I':
                self.input.append(0)
            case 'R':
                self.main.append(0)
            case 'O':
                self.output.append(0)

    
    def set_registre(self, rX:str, value:int):
        if rX not in self.content:
            args = rX.split("@")
            if len(args) > 1:
                rX = f"{args[0]}{self.get_registre(args[1])}"
        self.content[rX] = value
    
    def __repr__(self) -> str:
        
        return self.content.__repr__()


class MachineUniverselle:

    def __init__(self) -> None:
        self.registres = RegistreManager()
        self.tasks = []
        self.step = 0
    
    def get_config(self)-> tuple:
        return (self.step, self.registres)
    
    def next(self):
        if self.step < len(self.tasks):
            com, args = self.tasks[self.step]
            self.step = com(args)
            return True
        else:
            print("Machine Universel : End of program")
            return False

    def __get_value(self, arg) -> int:
        if type(arg) is str:
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
    
    def __JUMP(self, args):
        return args[0]
    
    def __JE(self, args):
        return args[2] if self.__get_value(args[0]) == self.__get_value(args[1]) else 1
    
    def __JLT(self, args):
        return args[2] if self.__get_value(args[0]) < self.__get_value(args[1]) else 1
    
    def __JGT(self, args):
        return args[2] if self.__get_value(args[0]) > self.__get_value(args[1]) else 1
    
    def start(self):
        number_of_tasks = len(self.tasks)
        print("Machine Universel : Start of program")
        while self.step < number_of_tasks:
            com, args = self.tasks[self.step]
            self.step += com(args)
        print("Machine Universel : End of program")
        print(self.registres)

    def build(self, path_of_ram_machine:str="example.ram"):
        """Build RAM Machine from .ram file"""
        print("Machine Universel : Build Started")
        command_finder = re.compile(r'[A-Z][A-Z]+')
        parenthese_finder = re.compile(r'\(|\)')
        integer_finder = re.compile(r'^[0-9]+$|^-[0-9]+$')

        with open(path_of_ram_machine,"r") as f:
            while (line:=f.readline()) != "":
                line = line.replace('\n','')
                x,y = command_finder.search(line).span()
                command = line[x:y] #########
                match command:
                    case 'ADD':
                        command = self.__ADD
                    case 'SUB':
                        command = self.__SUB
                    case 'MULT':
                        command = self.__MULT
                    case 'DIV':
                        command = self.__DIV
                    case 'MOD':
                        command = self.__MOD
                    case 'JUMP':
                        command = self.__JUMP
                    case 'JE':
                        command = self.__JE
                    case 'JLT':
                        command = self.__JLT
                    case 'JGT':
                        command = self.__JGT
                args = parenthese_finder.sub('',line[y:]).split(',')
                for i in range(len(args)):
                    if integer_finder.fullmatch(args[i]):
                        args[i] = int(args[i])
                task = (command, args)
                self.tasks.append(task)
        print("Machine Universel : Build finished")
    