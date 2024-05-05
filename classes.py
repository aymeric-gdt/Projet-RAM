import re
from time import time
from copy import deepcopy
import networkx as nx
import matplotlib.pyplot as plt

class RegistreManager:

    def __init__(self) -> None:
        self.lr_input = []
        self.lr_main = []
        self.lr_output = []

    def __extend(self, lr:list, x:int):
        while len(lr) < x+1:
            lr.append(0)
    
    def __in_lr(self, lr:list, x:int) -> bool:
        try:
            lr[x]
            return True
        except:
            return False
    
    def __select_lr(self, r):
        match r:
            case 'I':
                return self.lr_input
            case 'R':
                return self.lr_main
            case 'O':
                return self.lr_output

    def __getset(self,rX):
        args = rX.split("@")
        match len(args):
            case 2:
                r, x = self.__select_lr(args[0]), self.get_registre(args[1])
            case 1:
                r, x = self.__select_lr(args[0][0]), int(args[0][1:])
        if self.__in_lr(r,x) is False:
            self.__extend(r,x)
        return r,x

    def get_registre(self, rX:str)->int:
        r,x = self.__getset(rX)
        return r[x]

    def set_registre(self, rX:str, value:int):
        r,x = self.__getset(rX)
        r[x] = value
    
    def __repr__(self) -> str:
        output = 50*"*"+"\nREGISTRES:\n***INPUT***\n"
        for i, content in enumerate(self.lr_input):
            output += f"| I{i}={content} "
        output += "\n***MAIN***\n"
        for i, content in enumerate(self.lr_main):
            output += f"| R{i}={content} "
        output += "\n***OUTPUT***\n"
        for i, content in enumerate(self.lr_output):
            output += f"| O{i}={content} "
        return output+"\n"+50*"*"

class MachineUniverselle:

    def __init__(self) -> None:
        self.registres = RegistreManager()
        self.tasks = []
        self.pos = 0
        self.graph = nx.DiGraph()
    
    def load_input(self, data:list):
        data = [len(data)] + data
        print("Machine Universel : Start of Input Loading")
        t0 = time()
        for i, v in enumerate(data):
            self.registres.set_registre(f"I{i}", v)
        print(f"Machine Universel : Input Loaded in {round((time()-t0)*1000,1)}ms")
    
    def get_config(self)-> tuple:
        return (self.pos, deepcopy(self.registres))
    
    def set_config(self, new_pos, new_registres:RegistreManager):
        self.pos = new_pos
        self.registres = new_registres
    
    def next(self):
        if self.pos < len(self.tasks):
            com, args = self.tasks[self.pos]
            self.pos += com(args)
            return True
        else:
            print("Machine Universel : End of program")
            return False

    def __get_value(self, arg) -> int:
        if isinstance(arg, str):
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
        t0 = time()
        str =""
        for i in range(number_of_tasks):
            self.next()
            print("Etape:", i+1)
            str += f"Etape: {i+1}\n"
            print("Position:", self.pos)
            str += f"Position: {self.pos}\n"
            print(self.registres)
            str += f"{self.registres}\n"
        print(f"Machine Universel : Program finished in {round((time()-t0)*1000,1)}ms")
        str += f"Machine Universel : Program finished in {round((time()-t0)*1000,1)}ms"
        with open("output.txt","w") as f:
            f.write(str)

    def build(self, path_of_ram_machine:str="example.ram"):
        """Build RAM Machine from .ram file"""
        print("Machine Universel : Build Started")
        t0 = time()
        self.path = path_of_ram_machine
        command_finder = re.compile(r'[A-Z][A-Z]+')
        parenthese_finder = re.compile(r'\(|\)')
        integer_finder = re.compile(r'^[0-9]+$|^-[0-9]+$')
        with open(path_of_ram_machine,"r") as f:
            nodes = dict()
            while (line:=f.readline()) != "":
                line = line.replace('\n','')
                x,y = command_finder.search(line).span()
                args = parenthese_finder.sub('',line[y:]).split(',')
                for i in range(len(args)):
                    if integer_finder.fullmatch(args[i]):
                        args[i] = int(args[i])
                command = line[x:y]
                noeud = len(self.tasks)
                match command:
                    case 'ADD':
                        command = self.__ADD
                        nodes[noeud.__repr__()] = (f"{noeud.__repr__()}-ADD",[(noeud+1).__repr__()])
                    case 'SUB':
                        command = self.__SUB
                        nodes[noeud.__repr__()] = (f"{noeud.__repr__()}-SUB",[(noeud+1).__repr__()])
                    case 'MULT':
                        command = self.__MULT
                        nodes[noeud.__repr__()] = (f"{noeud.__repr__()}-MULT",[(noeud+1).__repr__()])
                    case 'DIV':
                        command = self.__DIV
                        nodes[noeud.__repr__()] = (f"{noeud.__repr__()}-DIV",[(noeud+1).__repr__()])
                    case 'MOD':
                        command = self.__MOD
                        nodes[noeud.__repr__()] = (f"{noeud.__repr__()}-MOD",[(noeud+1).__repr__()])
                    case 'JUMP':
                        command = self.__JUMP
                        nodes[noeud.__repr__()] = (f"{noeud.__repr__()}-JUMP",[(noeud+args[0]).__repr__()])
                    case 'JE':
                        command = self.__JE
                        nodes[noeud.__repr__()] = (f"{noeud.__repr__()}-JE",[(noeud+1).__repr__(), (noeud+args[2]).__repr__()])
                    case 'JLT':
                        command = self.__JLT
                        nodes[noeud.__repr__()] = (f"{noeud.__repr__()}-JLT",[(noeud+1).__repr__(), (noeud+args[2]).__repr__()])
                    case 'JGT':
                        command = self.__JGT
                        nodes[noeud.__repr__()] = (f"{noeud.__repr__()}-JGT",[(noeud+1).__repr__(), (noeud+args[2]).__repr__()])
                task = (command, args)
                self.tasks.append(task)
        self.nodes = nodes
        self.__build_graph()
        print(f"Machine Universel : Build finished in {round((time()-t0)*1000,1)}ms")

    def __build_graph(self):
        for _,v in self.nodes.items():
            name, sortants = v
            for s in sortants:
                try:
                    self.graph.add_edge(name, self.nodes[s][0])
                except KeyError:
                    pass

    def show_graph(self):
        print("Machine Universel : Graph : Start.")
        nx.draw_networkx(self.graph)
        plt.show()
        print("Machine Universel : Graph : End.")
    
    def dead_code_detector(self) -> list[int]:
        print("Machine Universel : dead-code-detector : Start.")
        output = []
        zero_in_degree_nodes = [node for node, in_degree in self.graph.in_degree() if in_degree == 0]
        if len(zero_in_degree_nodes) > 1:
            parcours_prof = nx.dfs_tree(self.graph, source=zero_in_degree_nodes[0])
            difference_graph_vs_parcours_prof = sorted(set(self.graph.edges())-set(parcours_prof.edges()))
            for c in difference_graph_vs_parcours_prof:
                c1, c2 = c
                c1 = int(c1.split('-')[0])
                c2 = int(c2.split('-')[0])
                if c1 < c2:
                    if len(output) == 0:
                        output.append(c1-1)
                    output.append(c1)
                    print(f"Machine Universel : dead-code-detector : line {c1+1} founded.")
            print("Machine Universel : dead-code-detector : End.")
        else:
            print("Machine Universel : dead-code-detector : Nothing to report.")
        return output
    
    def code_optimizer(self) -> str:
        print("Machine Universel : code-optimizer : Start.")
        with open(self.path,'r') as f:
            lines = f.readlines()
        # removing of dead-code
        for i in self.dead_code_detector():
            lines[i] = "\n"
        while True:
            try:
                lines.remove("\n")
            except ValueError:
                break
        # code-optimization
        pass
        # write a brand new optimized code
        path_split = self.path.split('/')
        file_split = path_split[-1].split('.')
        new_name = file_split[0]+"_optimized."+file_split[1]
        path_split[-1] = new_name
        new_path = "/".join(path_split)
        with open(new_path,"w") as f:
            f.writelines(lines)
        self.path = new_path
        print(f"Machine Universel : code-optimizer : optimized ram-code created at {self.path}")
        print("Machine Universel : code-optimizer : End.")
        return self.path


if __name__ == "__main__":
    print("classes.py : Nothing to run from here.")