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
  'len': 'LEN',
  'cap': 'CAP',
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

    #EDUARDO
  'type': 'TYPE',
  'continue': 'CONTINUE',
  'import': 'IMPORT',
  'return': 'RETURN',
  'var': 'VAR',
  'if': 'IF',
  'else': 'ELSE',
  'switch': 'SWITCH',
  'int': 'INTEGER',
  'int8': 'INT8',
  'int16': 'INT16',
  'int64': 'INT64',
  'float16': 'FLOAT16',
  'float32': 'FLOAT32',
  'complex64': 'COMPLEX64',
  'complex128': 'COMPLEX128',
  'uint8': 'UINT8',
  'uint16': 'UINT16',
  'uint32': 'UINT32',
  'uint64': 'UINT64'

}

tokens = [

    #GABRIEL
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

  #EDUARDO
  'NOTEQUALTO',
  'AND',
  'OR',
  'NOT',
  'GREATEROREQUAL',
  'LESSOREQUAL',
  'INCREMENT',
  'DECREMENT',
  'MODULUS',
  'LEFTKEY',
  'RIGHTKEY',
  'IGNORE',

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
t_MODULUS = r'%'
t_GREATEROREQUAL = r'>='
t_LESSOREQUAL = r'<='
t_LEFTKEY = r'\{'
t_RIGHTKEY = r'\}'

#EDUARDO
t_DOT = r'\.'
t_IGNORE = r' \t'
t_COLON = r':'
t_SEMICOLON = r';'
t_ARROBA = r'\@'
t_NUMERAL = r'\#'
t_BACKSLASH = r'\\'
t_AMPERSON = r'\&'
t_COMMA = r','
t_LCOR = r'\['
t_RCOR = r'\]'
t_ignore = ' \t'

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


#EDUARDO
#Agregue conteo de lineas
def t_newline(t):
  r'\n+'
  t.lexer.lineno += len(t.value)


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
"""
def getTokens(lexer):
  for tok in lexer:
    print(tok)
file = open("source.txt")
#EDUARDO
for line in file:
  lexer.input(line)
  getTokens(lexer)
"""