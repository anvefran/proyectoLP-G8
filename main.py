import ply.yacc as yacc
from lexico import tokens


#CUERPO
def p_cuerpo(p):
  '''cuerpo : asignacion
  | operacion
  | comparacion
  | slice
  | sliceMethods
  | impresion
  '''


#DECLARACIONES
def p_asignacion(p):
  'asignacion : VARIABLE COLON IGUAL valor'


def p_valor(p):
  '''valor : ENTERO
  | FLOAT
  | STR '''


#EXPRESIONES: operaciones y comparaciones
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


#ESTRUCTURAS DE DATOS: reglas sintácticas para declarar estructuras, es posible invocar a sus métodos.
def p_slice(p):
  '''slice : VARIABLE COLON IGUAL LCOR RCOR datatype LEFTKEY elementos RIGHTKEY
  | VARIABLE COLON IGUAL LCOR RCOR datatype LEFTKEY RIGHTKEY
  '''


def p_datatype(p):
  '''datatype : STRING
  | INTEGER
  | BOOL
  | INT32
  | UINT
  | INT8
  | INT16
  | INT64
  | FLOAT16
  | FLOAT32
  '''


def p_elementos(p):
  '''elementos : valor
  | VARIABLE
  | valor COMMA elementos
  | VARIABLE COMMA elementos
  '''


#slice metodos para hallar la longitud y capacidad de un slice
def p_sliceMethods(p):
  '''sliceMethods  : LEN LPAREN VARIABLE RPAREN
  | CAP LPAREN VARIABLE RPAREN
  '''


#FUNCIONES declaracion


#funciones imprimir y entrada de datos
def p_impresion(p):
  '''impresion : FMT DOT PRINT LPAREN elementos RPAREN'''


#ESTRUCTURAS DE CONTROL:Tienen reglas sintácticas para selección y repetición. Se pueden anidar, agregar al cuerpo otras reglas.


#EXTRA
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
