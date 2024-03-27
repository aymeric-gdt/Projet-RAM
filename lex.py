######################################### LIB #########################################

import ply.lex as lex
import ply.yacc as yacc

######################################### LEX #########################################

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
}

tokens = ['NUMBER', 'ID'] + list(reserved.values())

def t_ID(t):
    r'\@|[a-zA-Z_][a-zA-Z_]*'
    t.type = reserved.get(t.value,'ID')    # Check for reserved words
    return t

def t_REGISTRE(t):
    r'R|I|[0-9]+'

    t.value = t.value

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

######################################### YACC #########################################

def p_result_add(p):
    'result : ADD NUMBER NUMBER REGISTRE_O NUMBER'
    p[0] = p[2] + p[3]

def p_RegistreIn_registre_i(p):
    'RegistreIn : REGISTRE_I NUMBER'
    p[0] = p[2] + p[3]

def p_error(p):
    print("Syntax error in input!")

# Build the parser
parser = yacc.yacc()

######################################### MAIN #########################################

with open("test.ram","r") as f:
    while (line:=f.readline()) != "":
        parser.parse(line,lexer=lexer)

#with open("test.ram","r") as f:
#    while (line:=f.readline()) != "":
#        print(line)
#        lexer.input(line)
#        while (tok:=lexer.token()):
#            print(tok)