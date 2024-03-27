import re

command_to_operation = {
    'ADD' : lambda x, y : x + y,
    'SUB' : lambda x, y : x - y,
    'MULT' : lambda x, y : x * y,
    'DIV' : lambda x, y : x // y,
    'MOD' : lambda x, y : x % y
}

#def operation(operation:str,x:'Registre|int', y:'Registre|int', z:'Registre') -> int:
#    z.set_value(command_to_operation.get(operation)(x.get_value() if type(x) is Registre else x, y.get_value() if type(y) is Registre else y))
#    return 1

def operation(args) -> int:
    command = args[0]
    if (entry_size:=len(args)) == 2:
        if command == 'JUMP':
            return args[1]
    elif entry_size == 4:
        x = args[1].get_value() if type(args[1]) is Registre else args[1]
        y = args[2].get_value() if type(args[2]) is Registre else args[2]
        z = args[3].get_value() if type(args[3]) is Registre else args[3]
        if command == 'JE':
            return z if x == y else 1
        elif command == 'JLT':
            return z if x < y else 1
        elif command == 'JGT':
            return z if x > y else 1
        else:
            args[3].set_value(command_to_operation.get(command)(x,y))
            return 1
    else:
        raise SyntaxError


class Registre:

    def __init__(self, name:str) -> None:
        self.__value = 0
        self.__name = name
    
    def get_name(self)-> str:
        return self.__name

    def get_value(self) -> int:
        return self.__value
    
    def set_value(self, new_value:int):
        self.__value = new_value

    def __repr__(self) -> str:
        return f'{self.__name} : {self.__value}'


class RegistreManager:

    def __init__(self) -> None:
        self.__registres = []
    
    def get_registre_from_name(self, rX:str) -> Registre:
        for registre in self.__registres:
            if registre.get_name() == rX:
                return registre
        self.add_registre(rX)
        return self.__registres[-1]

    def add_registre(self, rX:str):
        self.__registres.append(Registre(rX))
    
    def __repr__(self) -> str:
        out = ""
        for registre in self.__registres:
            out += registre.__repr__()+" | "
        return out



class MachineUniverselle:

    def __init__(self) -> None:
        self.registre_manager = RegistreManager()
        self.tasks = []
        self.step = 0
    
    def print_tasks(self):
        for task in self.tasks:
            print(task)
    
    def build(self,path_of_ram_machine:str="test.ram"):
        """Build RAM Machine from .ram file"""
        commande_finder = re.compile(r'[A-Z][A-Z]+')
        parenthese_finder = re.compile(r'\(|\)')
        integer_finder = re.compile(r'^[0-9]+$|^-[0-9]+$')

        with open(path_of_ram_machine,"r") as f:
            while (line:=f.readline()) != "":
                line = line.replace('\n','')
                x,y = commande_finder.search(line).span()
                com = line[x:y]
                args = parenthese_finder.sub('',line[y:]).split(',')
                for i in range(len(args)):
                    if integer_finder.fullmatch(args[i]):
                        args[i] = int(args[i])
                    else:
                        args[i] = self.registre_manager.get_registre_from_name(args[i])
                task = tuple([com]+args)
                self.tasks.append(task)

    def set_input(self,data:list):
        pass

    def resolve(self):
        while self.step < len(self.tasks):
            self.step += operation(self.tasks[self.step])
            print(self.registre_manager)
            print(self.step)
