class RegistryContainer:

    def __init__(self) -> None:
        """initialise un RegistryContainer vide"""
        self.__content = list()

    def add_registry(self):
        """ajoute un registre au RegistryContainer avec la valeur 0 (par défaut)"""
        self.__content.append(0)

    def read_registry(self,index:int) -> int:
        """lecture du registre i du RegistryContainer"""
        return self.__content[index]
    
    def write_registry(self,index:int,value:int) -> None:
        """écriture sur le registre i du RegistryContainer"""
        self.__content[index] = value

    def __repr__(self) -> str:
        return self.__content.__repr__()


class InputRegistryContainer(RegistryContainer):

    def __init__(self) -> None:
        """Read Only"""
        super().__init__()
        self.add_registry()

    def load_data(self, data: list):
        """Permet de charger des données dans votre InputRegistryContainer"""
        super().write_registry(index=0,value=len(data))
        for i,r in enumerate(data,1):
            super().add_registry()
            super().write_registry(index=i,value=r)
    
    def write_registry(self, index: int, value: int) -> None:
        raise TypeError("InputRegistryContainer is read only")


class OutputRegistryContainer(RegistryContainer):

    def __init__(self) -> None:
        """Write Only"""
        super().__init__()
    
    def read_registry(self, index: int) -> int:
        raise TypeError("OutputRegistryContainer is write only")


class MachineUniverselle:

    def __init__(self) -> None:
        self.I = InputRegistryContainer()
        self.R = RegistryContainer()
        self.O = OutputRegistryContainer()
    
    def build(self,path_of_ram_machine:str="example.ram"):
        with open(path_of_ram_machine,"r") as f:
            f.readline()

    def set_input(self,data:list):
        pass

    def start(self):
        pass

MU = MachineUniverselle()
MU.build()