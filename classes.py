import ply.lex as lex
import ply.yacc as yacc

command_to_operation = {
    'ADD' : lambda x, y : x + y,
    'SUB' : lambda x, y : x - y,
    'MULT' : lambda x, y : x * y, 
    'DIV' : lambda x, y : x // y,
    'MOD' : lambda x, y : x % y
}

def operation(operation:str,x:'Registre|int', y:'Registre|int', z:'Registre') -> int:
    z.set_value(command_to_operation.get(operation)(x.get_value() if type(x) is Registre else x, y.get_value() if type(y) is Registre else y))
    return 1


class Registre:

    def __init__(self) -> None:
        self.__value = 0
    
    def get_value(self) -> int:
        return self.__value
    
    def set_value(self, new_value:int):
        self.__value = new_value

    def __repr__(self) -> str:
        return self.__value.__repr__()


class RegistreManager:

    def __init__(self) -> None:
        self.__name_to_index = dict()
        self.__registres = []
    
    def get_registre_from_name(self, rX:str) -> Registre:
        if (index:=self.__name_to_index.get(rX, -1)) > -1:
            return self.__registres[index]
        else:
            self.add_registre(rX)
            return self.get_registre_from_name(rX)

    def add_registre(self, rX:str):
        self.__name_to_index[rX] = len(self.__registres)
        self.__registres.append(Registre())
    
    def __repr__(self) -> str:
        out = ""
        for name, index in self.__name_to_index.items():
            out += f"{name} : {self.__registres[index]} | "
        return out



class MachineUniverselle:

    def __init__(self) -> None:
        self.I = []
        self.R = []
        self.O = []
        self.tasks = []
        self.step = 0
    
    def build(self,path_of_ram_machine:str="test.ram"):
        """Build RAM Machine from .ram file"""
        pass

    def set_input(self,data:list):
        for elem in data:
            self.I.append(Registre())
            self.I[-1].set_value(elem)

    def start(self):
        #self.tasks.append((sum, (2,4,7)))
        i = 0
        while len(self.tasks) > i:
            com, args = self.tasks[i]
            i += com(args)



MU = MachineUniverselle()
MU.build()