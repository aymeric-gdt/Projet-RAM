import ply.lex as lex

reserved = {
   # OPERATIONS
   'ADD' : 'ADD',
   'SUB' : 'SUB',
   'DIV' : 'DIV',
   'MULT' : 'MULT',
   'MOD' : 'MOD',
   # REFERENCE
   '@' : 'REFERENCE',
   # JUMPS
   'JUMP' : 'JUMP',
   'JE' : 'JE',
   'JLT' : 'JLT',
   'JGT' : 'JGT',
   # PARENTHESES
   '(' : 'LPAREN',
   ')' : 'RPAREN',
   # LES REGISTRES
   'I' : 'REGISTRE_I',
   'R' : 'REGISTRE_R',
   'O' : 'REGISTRE_O'
}

tokens = ['NUMBER', 'ID'] + list(reserved.values())

def t_ID(t):
    r'\@|[a-zA-Z_][a-zA-Z_]*'
    t.type = reserved.get(t.value,'ID')    # Check for reserved words
    return t

def t_NUMBER(t):
    r'\-?[0-9]'
    t.value = int(t.value)
    return t

def t_error(t):
   if t.value[0] not in ['(',')',',','\n']:
      print("Illegal character '%s'" % t.value[0])
   t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

with open("example.ram","r") as f:
    while (line:=f.readline()) != "":
        print(line)
        lexer.input(line)
        while (tok:=lexer.token()):
            print(tok)