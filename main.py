from classes import MachineUniverselle
import random as rd

tests = ["deadcode_example.ram",
         "apowb.ram",
         "triabulle.ram"]

mu = MachineUniverselle()
mu.load_input([rd.randint(0,10) for _ in range(10)])
mu.build("ram/"+tests[2])
#mu.show_graph()
mu.start()
