from classes import MachineUniverselle
import random as rd
import sys
from tkinter.filedialog import askopenfilename

# Question 2
def test_next():
    print("main.py : Test de l'éxecution pas à pas sur apowb.ram.")
    print("main.py : calcul de 2**5")
    step = int(input("Choisir le nombre d'étapes à effectuer : "))
    mu.load_input([2, 5])
    mu.build("ram/apowb.ram")
    i = 0
    while mu.next():
        print("Etape:", i)
        print("Position:", mu.pos)
        print(mu.registres)
        i+=1
        if i == step:
            print("main.py : l'execution s'arrête.")
            break

# Question 5
def test_apowb():
    print("main.py : Test de la machine universelle avec le programme apowb.ram")
    a = int(input("Veuillez saisir un entier a : "))
    b = int(input("Veuillez saisir un entier b : "))
    mu.load_input([a,b])
    mu.build("ram/apowb.ram")
    mu.start()

# Question 5
def test_triabulle():
    print("main.py : Test de la machine universelle avec le programme triabulle.ram")
    to_sort = [rd.randint(0,10) for _ in range(10)]
    print(f"main.py : 10 nombres générés aléatoirement à trier : {to_sort}")
    mu.load_input(to_sort)
    mu.build("ram/triabulle.ram")
    mu.start()

# Question 6/7
def test_automate(mot:list, transitions:list):
    print("Test de la machine universelle avec le programme automate.ram")
    liste = []
    liste += [len(mot)]
    liste += [(len(transitions) // 6) + 1]
    liste += mot
    liste += transitions
    mu.load_input(liste)
    mu.build("ram/automate.ram")
    mu.start()

# Question 8
def test_graph():
    print("Test de la fonctionnalité d'affichage de graphe")
    mu.build(askopenfilename(defaultextension=".ram", initialdir="./ram", initialfile= "apowb.ram"))
    mu.show_graph()

# Question 9/10

def test_dead_code():
    print("Test de la détection de code mort dans un programme")
    mu.build(askopenfilename(defaultextension=".ram", initialdir="./ram", initialfile= "apowb.ram"))
    mu.dead_code_detector()


if __name__ == "__main__":
    mu = MachineUniverselle()
    print("main.py : Start.")
    msg = '''Veuillez relancer le code python avec un des arguments suivant : 
    "a**b", "step-by-step", "bubble-sort", "automate", "graph", "code-mort". '''
    try:
        match sys.argv[1]:
            case "step-by-step":
                test_next()
            case "a**b":
                test_apowb()
            case "bubble-sort":
                test_triabulle()
            case "automate":
                test_automate([1,1,1,1,0,0,0,0], [0,0,0,1,1,2,2,0,1,1,1,2,2,1,1,0,0,3,3,1,1,0,0,3,3,1,0,0,0,1])
            case "graph":
                test_graph()
            case "code-mort":
                test_dead_code()
            case _:
                print(msg)
    except IndexError:
        print(msg)
    print("main.py : End.")