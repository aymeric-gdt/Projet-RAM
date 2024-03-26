import ply.lex

# Z pouvant être un registre ou un entier positif

tokens = (
   'ADD',        # ADD(Za,Zb, Registre)
   'SUB',        # SUB(Za,Zb, Registre)
   'DIV',        # DIV(Za,Zb, Registre), division entière
   'MULT',       # MULT(Za,Zb, Registre)
   'MOD',        # MOD(Za,Zb, Registre)

   'JUMP',       # JUMP(Z)
   'JE',         # JUMP IF EQUAL
   'JLT',        # JUMP IF LOWER THAN
   'JGT',        # JUMP IF GREATER THAN

   'NOMBRE',     # Entier relatif"

   'REGISTRE_I',
   'REGISTRE_R',
   'REGISTRE_O',

   'LPAREN',     # Parenthèse gauche
   'RPAREN',     # Parenthèse droite
)

t_ADD = r'ADD'
t_SUB = r'SUB'
t_DIV = r'DIV'
t_MULT = r'MULT'
t_MOD = r'MOD'

t_JUMP = r'JUMP'
t_JE = r'JE'
t_JLT = r'JLT'
t_JGT = r'JGT'

t_NOMBRE = r'\-?[0-9]'

t_REGISTRE_I = r'I'
t_REGISTRE_R = r'R'
t_REGISTRE_O = r'O'

t_LPAREN = r'\('
t_RPAREN = r'\)'



