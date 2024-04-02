import ram_to_python
from tkinter.filedialog import askopenfilename
import pathlib

if (filename:=askopenfilename(initialdir=pathlib.Path().resolve())):
    ram_to_python.main(filename)
else:
    print("End of program")