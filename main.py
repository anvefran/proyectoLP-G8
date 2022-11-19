import ply.yacc as yacc
from lexico import tokens


#CUERPO
def p_cuerpo(p):
  '''cuerpo : asignacion
  | operacion
  | comparacion'''


#declaraciones
def p_asignacion(p):
  'asignacion : VARIABLE COLON IGUAL valor'


def p_valor(p):
  '''valor : ENTERO
  | FLOAT
  | STR '''


#expresiones: operaciones y comparaciones
#faltan las opciones de que sea 2+variable o 2+2
def p_operacion(p):
  '''operacion : VARIABLE operadorOp VARIABLE
  | VARIABLE incDec '''


def p_operadorOp(p):
  '''operadorOp : PLUS
  | MINUS
  | TIMES
  | DIVIDE
  | MODULUS '''


def p_incDec(p):
  '''incDec : INCREMENT
  | DECREMENT '''


def p_comparacion(p):
  '''comparacion : VARIABLE operadorCmp VARIABLE
  | valor operadorCmp valor'''


def p_operadorCmp(p):
  '''operadorCmp : NOTEQUALTO
  | GREATEROREQUAL
  | LESSOREQUAL
  '''


def p_error(p):
  if p:
    print(
      f"Error de sintaxis - Token: {p.type}, Línea: {p.lineno}, Col: {p.lexpos}"
    )
    parser.errok()
  else:
    print("Error de sintaxis Fin de Linea")


# Build the parser
parser = yacc.yacc()


def validaRegla(s):
  result = parser.parse(s)
  print(result)


while True:
  try:
    s = input('calc > ')
  except EOFError:
    break
  if not s: continue
  validaRegla(s)
