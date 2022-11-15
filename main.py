
import ply.lex as lex

reservado = {
    #Gabriel
  'struct': 'STRUCTURE',
  'chan': 'CHANNEL',
  'goto': 'GOTO',
  'package': 'PACKAGE',
  'const': 'CONSTANT',
  'fallthrough': 'FALLTHROUGH',
  'range': 'RANGE',
  'rune': 'RUNE',
  'int32': 'INT32',
  'byte': 'BYTE',
  'uint': 'UINT',
  'fmt': 'FMT',
  'string': 'STRING',
  'make': 'MAKE',
  #ANDREA
  'break': 'BREAK',
  'default': 'DEFAULT',
  'func': 'FUNCTION',
  'interface': 'INTERFACE',
  'select': 'SELECT',
  'case': 'CASE',
  'defer': 'DEFER',
  'go': 'GO',
  'map': 'MAP',
  'for': 'FOR',
  'bool': 'BOOL',
  'Print': 'PRINT',
  'Println': 'PRINTLN',
  'Scanf': 'SCANF',

}

tokens = [
    #Gabriel
  'ENTERO',
  'FLOAT',
  'BOOLEAN',
  'STR',
  'MINUS',
  'PLUS',
  'TIMES',
  'DIVIDE',
  'LPAREN',
  'RPAREN',
  'VARIABLE',
  'IGUAL',
  'GREATERTHAN',
  'LESSTHAN',
  'EQUALTO',
  #ANDREA
  'COLON',
  'DOT',
  'ARROBA',
  'NUMERAL',
  'BACKSLASH',
  'AMPERSON',
  'RCOR',
  'LCOR',
  'SEMICOLON',
  'COMMA',
] + list(reservado.values())

#Gabriel
t_PLUS = r'\+'
t_MINUS = r'\-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_IGUAL = r'='
t_GREATERTHAN = r'>'
t_LESSTHAN = r'<'
t_EQUALTO = r'=='
t_LPAREN = r'\('
t_RPAREN = r'\)'

#ANDREA
t_NOTEQUALTO = r'!='
t_AND = r'\&\&'
t_OR = r'\|\|'
t_NOT = r'!'
t_INCREMENT = r'\+\+'
t_DECREMENT = r'\-\-'
t_MODULUS = r'\%'
t_GREATEROREQUAL = r'>='
t_LESSOREQUAL = r'<='
t_LEFTKEY = r'\{'
t_RIGHTKEY = r'\}'

#Gabriel
def t_FLOAT(t):
  r'\d+\.\d+'
  t.value = float(t.value)
  return t


def t_ENTERO(t):
  r'\d+'
  t.value = int(t.value)
  return t


def t_BOOLEAN(t):
  r'true|false'
  return t


def t_STR(t):
  r'("[^"]*")'
  return t


def t_VARIABLE(t):
  r'[a-zA-Z_][a-zA-Z0-9]*'
  t.type = reservado.get(t.value, 'VARIABLE')
  return t

#ANDREA
#Agregue token de ignorar
def t_COMMENTS(t):
  r'\/\/.+|^\/\.+\\/$'
  pass


#Agregue token de error
def t_error(t):
  print("Caracter no permitido '%s'" % t.value[0])
  t.lexer.skip(1)

#Gabriel
lexer = lex.lex()

def getTokens(lexer):
  for tok in lexer:
    print(tok)


file = open("source.txt")
