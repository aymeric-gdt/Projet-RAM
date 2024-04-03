import ram_to_python
from classes import MachineUniverselle
from tkinter.filedialog import askopenfilename
import pathlib

mu = MachineUniverselle()
mu.build()
mu.start()
