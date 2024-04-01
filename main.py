import lex_yacc
from tkinter.filedialog import askopenfilename
import pathlib

if (filename:=askopenfilename(initialdir=pathlib.Path().resolve())):
    lex_yacc.main(filename)
else:
    print("End of program")