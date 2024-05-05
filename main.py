from classes import MachineUniverselle
import random as rd
from tkinter.filedialog import askopenfilename

#Question 2
def test_next(step):
    print("Test de la machine universelle avec le programme apowb.ram")
    mu = MachineUniverselle()
    mu.load_input([rd.randint(0,10) for _ in range(2)])
    mu.build("ram/apowb.ram")

    length = len(mu.tasks)
    
    if step > length:
        print(f"Erreur : {step} > {length} (max d'étapes)")
    else:
        for i in range(step):
            mu.next()
            print("Etape:", i+1)
            print("Position:", mu.pos)
            print(mu.registres)

# Question 5
def test_apowb():
    print("Test de la machine universelle avec le programme apowb.ram")
    mu = MachineUniverselle()
    mu.load_input([rd.randint(0,10) for _ in range(2)])
    mu.build("ram/apowb.ram")
    mu.start()

# Question 5
def test_triabulle():
    print("Test de la machine universelle avec le programme triabulle.ram")
    mu = MachineUniverselle()
    mu.load_input([rd.randint(0,10) for _ in range(10)])
    mu.build("ram/triabulle.ram")
    mu.start()

# Question 6/7
def test_automate(mot:list, transitions:list):
    print("Test de la machine universelle avec le programme automate.ram")
    mu = MachineUniverselle()
    liste = []
    liste += mot
    liste += transitions
    print(liste)
    mu.load_input(list)
    mu.build("ram/automate.ram")
    mu.start()

# Question 8
def test_graph():
    print("Test de l'affichage du graphe du programme apowb.ram")
    mu = MachineUniverselle()
    mu.load_input([rd.randint(0,10) for _ in range(10)])
    mu.build("ram/apowb.ram")
    mu.show_graph()

# Question 9/10

def test_dead_code():
    print("Test de la détection de code mort dans le programme deadcode_example.ram")
    mu = MachineUniverselle()
    mu.load_input([rd.randint(0,10) for _ in range(10)])
    mu.build("ram/deadcode_example.ram")
    mu.dead_code_detector()

def test_dead_code_opti():
    print("Test de la détection de code mort dans le programme deadcode_example_optimized.ram")
    mu = MachineUniverselle()
    mu.load_input([rd.randint(0,10) for _ in range(10)])
    mu.build("ram/deadcode_example_optimized.ram")
    mu.dead_code_detector()


if __name__ == "__main__":
    #Enlevez les commentaires pour tester les fonctions :

    #test_next(6)
    #test_apowb()
    #test_triabulle()
    #test_automate([1,1,1,1,0,0,0,0, [0,0,0,1,1,2,2,0,1,1,1,2,2,1,1,0,0,3,3,1,1,0,0,3,3,1,0,0,0,1])
    #test_graph()
    #test_dead_code()
    #test_dead_code_opti()

    print("main.py : End.")
