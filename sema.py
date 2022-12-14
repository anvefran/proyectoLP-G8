import ply.yacc as yacc
import sys
from lexico import tokens
from datetime import datetime

global listaerr
listaerr = []

#CUERPO (Andrea-Gabriel-Eduardo)
def p_cuerpo(p):
  '''cuerpo : asignacion
  | asignacion cuerpo
  | inicio
  | inicio cuerpo
  | operacion
  | operacion cuerpo
  | comparacion
  | comparacion cuerpo
  | slice
  | slice cuerpo
  | sliceMethods
  | sliceMethods cuerpo
  | impresion
  | impresion cuerpo
  | conditional_structure
  | conditional_structure cuerpo
  | arrays
  | arrays cuerpo
  | maps
  | maps cuerpo
  | mapelem
  | mapelem cuerpo
  | input
  | input cuerpo
  | impresionln
  | impresionln cuerpo
  | funcion
  | funcion cuerpo
  '''

def p_inicio(p):
  '''inicio : IMPORT STR
  | IMPORT LPAREN STR RPAREN
  | PACKAGE VARIABLE'''

  #Gabriel, Andrea y Eduardo
  #DECLARACIONES
def p_asignacion(p):
  '''asignacion : VARIABLE COLON IGUAL valor
  | VAR VARIABLE datatype 
  | VAR VARIABLE tipo_asignacion
  '''
#ANDREA
#SEMANTICO: 1 Se puede asignar un tipo de dato a una variable que contenga el mismo tipo de dato declarado.
#var x int = 3
#var cadena string = "Hola"
#var decimal float = 3.2

def p_tipo_asignacion(p):
  '''tipo_asignacion : INT32 IGUAL ENTERO
  | FLOAT16 IGUAL FLOAT
  | STRING IGUAL STR
  | INTEGER IGUAL ENTERO
  '''
#GABRIEL
#SEMANTICO: 2 casting de enteros a floats
#Solo puede ser usado cuando se declara una variable
# conversion := float32(35)
# conversion2 := float16(15)
def p_int_casting(p):
  '''int_casting : FLOAT16 LPAREN ENTERO RPAREN
  | FLOAT32 LPAREN ENTERO RPAREN
  '''

#tipos de datos - Eduardo
def p_datatype(p):
  '''datatype : INT32
  | BYTE
  | UINT
  | STRING
  | INTEGER
  | INT8
  | INT16
  | INT64
  | FLOAT16
  | FLOAT32
  | COMPLEX64
  | COMPLEX128
  | UINT8
  | UINT16
  | UINT32
  | UINT64
  | BOOL'''

#Posibles asignaciones para una variable - Andrea
def p_valor(p):
  '''valor : ENTERO
  | FLOAT
  | STR 
  | int_casting'''

def p_numero(p):
  '''numero : ENTERO
  | FLOAT'''

#ANDREA
#EXPRESIONES: operaciones y comparaciones - Andrea
#SEMANTICO 3: OPERACIONES DEBEN REALIZARSE CON EL MISMO TIPO
def p_operacion(p):
  '''operacion : VARIABLE incDec 
  | VARIABLE operadorOp valor
  | VARIABLE PLUS IGUAL valor
  | VARIABLE PLUS IGUAL VARIABLE
  | operacionNUM
  | operacionSTR
  '''
def p_operacionNUM(p):
  '''operacionNUM : numero operadorOp masNumeros'''
def p_masNumeros(p):
  '''masNumeros : numero
  | VARIABLE
  | numero operadorOp masNumeros
  | VARIABLE operadorOp masNumeros'''

def p_operacionSTR(p):
  '''operacionSTR : STR operadorOp masSTR'''
def p_masSTR(p):
  '''masSTR : STR
  | VARIABLE
  | STR operadorOp masSTR
  | VARIABLE operadorOp masSTR'''
  
def p_operadorOp(p):
  '''operadorOp : PLUS
  | MINUS
  | TIMES
  | DIVIDE
  | MODULUS '''

def p_incDec(p):
  '''incDec : INCREMENT
  | DECREMENT '''

#Gabriel
  #SEMANTICO 4: Las comparaciones solo se pueden realizar al mismo tipo de dato.
  #Ejemplo : 1>2, "HOLA"<= "hola", no puede existir 1>"hola"


def p_comparacion(p):
  '''comparacion : VARIABLE operadorCmp VARIABLE
  | STR operadorCmp STR
  | FLOAT operadorCmp FLOAT
  | ENTERO operadorCmp ENTERO
  | VARIABLE operadorCmp STR
  | STR operadorCmp VARIABLE
  | ENTERO operadorCmp VARIABLE
  | VARIABLE operadorCmp ENTERO
  | FLOAT operadorCmp VARIABLE
  | VARIABLE operadorCmp FLOAT'''

def p_operadorCmp(p):
  '''operadorCmp : NOTEQUALTO
  | GREATEROREQUAL
  | LESSOREQUAL
  | GREATERTHAN
  | LESSTHAN
  | EQUALTO
  '''

#ESTRUCTURAS DE CONTROL
#Gabriel y Eduardo
def p_conditional_structure(p):
  '''conditional_structure : IF LPAREN comparacion RPAREN LEFTKEY conditional_block RIGHTKEY
  | IF LPAREN comparacion RPAREN LEFTKEY conditional_block RIGHTKEY elif_structure
  | IF LPAREN comparacion RPAREN LEFTKEY conditional_block RIGHTKEY ELSE LEFTKEY conditional_block RIGHTKEY
  | IF comparacion LEFTKEY conditional_block RIGHTKEY
  | IF comparacion LEFTKEY conditional_block RIGHTKEY elif_structure
  | IF  comparacion LEFTKEY conditional_block RIGHTKEY ELSE LEFTKEY conditional_block RIGHTKEY
  | FOR asignacion SEMICOLON comparacion SEMICOLON operacion LEFTKEY forbody RIGHTKEY
  | SWITCH asignacion SEMICOLON VARIABLE LEFTKEY cuerposwitchin RIGHTKEY
  | SWITCH VARIABLE LEFTKEY cuerposwitchin RIGHTKEY'''

#Gabriel y Eduardo
def p_elif_structure(p):
  '''elif_structure : ELSE IF LPAREN comparacion RPAREN LEFTKEY conditional_block RIGHTKEY
  | ELSE IF LPAREN comparacion RPAREN LEFTKEY conditional_block RIGHTKEY elif_structure
  | ELSE IF LPAREN comparacion RPAREN LEFTKEY conditional_block RIGHTKEY ELSE LEFTKEY conditional_block RIGHTKEY'''

#El contenido de un bloque condicional
def p_conditional_block(p):
  'conditional_block : cuerpo'

#Gabriel
def p_cuerposwitchin(p):
  '''cuerposwitchin : CASE valor COLON cuerpo
  | CASE valor COLON cuerpo cuerposwitchin
  | CASE valor COLON cuerpo cuerposwitchin default
  '''
def p_default(p):
  ''' default : DEFAULT COLON cuerpo
  | DEFAULT COLON'''
  
def p_forbody(p):
  '''forbody : cuerpo
  | FOR asignacion SEMICOLON comparacion SEMICOLON operacion LEFTKEY cuerpo RIGHTKEY
  '''

#ESTRUCTURAS DE DATOS: reglas sint??cticas para declarar estructuras, es posible invocar a sus m??todos.
#Andrea
def p_slice(p):
  '''slice : VARIABLE COLON IGUAL LCOR RCOR datatype LEFTKEY elementos RIGHTKEY
  | VARIABLE COLON IGUAL LCOR RCOR datatype LEFTKEY RIGHTKEY
  '''

def p_arrays(p):
  'arrays : VAR VARIABLE LCOR ENTERO RCOR datatype'

def p_elementos(p):
  '''elementos : valor
  | VARIABLE
  | valor COMMA elementos
  | VARIABLE COMMA elementos
  '''

#Gabriel
def p_maps(p):
  '''maps : VARIABLE COLON IGUAL MAKE LPAREN MAP LCOR datatype RCOR datatype RPAREN
  '''

def p_mapelem(p):
  '''mapelem : VARIABLE LCOR valor RCOR
  | VARIABLE LCOR valor RCOR IGUAL valor
  '''

#slice metodos para hallar la longitud y capacidad de un slice, Andrea
def p_sliceMethods(p):
  '''sliceMethods  : LEN LPAREN VARIABLE RPAREN
  | CAP LPAREN VARIABLE RPAREN
  '''

#Funciones - Eduardo Salavarr??a
#1er caso: funciones sin argumentos, sin retornos "func variable()(){body}"
#2do caso: con retorno sin argumentos
#3er caso: sin retorno con n argumentos
#4to caso: con retorno, con argumentos
#Psdt: en el mismo sint??ctico se valida que la funci??n retorne un elemento en caso que haya sido declarado como funci??n con elementos de retorno


#EDUARDO
#Semantico 5: Funciones que tengan par??ntesis de retorno debe poseer la palabra reservada return.

#Semantico 6: Funciones que tenga un tipo de dato de retorno tendr??n que devolver el mismo tipo de dato de retorno

def p_funcion(p):
  '''funcion : FUNCTION VARIABLE LPAREN RPAREN LPAREN RPAREN LEFTKEY cuerpo RIGHTKEY
  | FUNCTION VARIABLE  LPAREN  RPAREN LPAREN freturns RPAREN LEFTKEY fbody_wreturn RIGHTKEY
  | FUNCTION VARIABLE  LPAREN  farguments RPAREN LPAREN RPAREN LEFTKEY cuerpo RIGHTKEY
  | FUNCTION VARIABLE LPAREN farguments RPAREN LPAREN INT32 RPAREN LEFTKEY fbody_int_return RIGHTKEY
  | FUNCTION VARIABLE LPAREN farguments RPAREN LPAREN STRING RPAREN LEFTKEY fbody_str_return RIGHTKEY'''

#funcion que apoya a "funcion"  declara funciones single-argument y multiple-argument
def p_farguments(p):
  '''farguments : VARIABLE datatype
  | VARIABLE datatype COMMA farguments'''

#funci??n de apoyo a "funcion" permite que las funciones tenga uno o m??ltiple retornos
def p_freturns(p):
  '''freturns : datatype
  | datatype COMMA freturns'''

def p_fbody_str_return(p):
  'fbody_str_return : cuerpo RETURN STR'

def p_fbody_int_return(p):
  'fbody_int_return : cuerpo RETURN ENTERO'

#cuerpo de la funci??n con retorno (debe tener una linea return a, b, ...)
def p_fbody_wreturn(p):
  '''fbody_wreturn : cuerpo RETURN VARIABLE
  | cuerpo RETURN elementos
  | RETURN elementos'''

#funciones imprimir y entrada de datos
#Gabriel y Andrea
def p_impresion(p):
  '''impresion : FMT DOT PRINT LPAREN elementos RPAREN
  | FMT DOT PRINTLN LPAREN elementos RPAREN
  '''

#Gabriel
def p_input(p):
  '''input : FMT DOT SCANF LPAREN datatype COMMA VARIABLE RPAREN
  '''

#Eduardo
#M??todo para mostrar en pantalla (Coloca un salto de l??nea al final de la cadena de caracteres)
def p_impresionln(p):
  '''impresionln : FMT DOT PRINTLN LPAREN impresion_content RPAREN'''

#Contiene el contenido de la funci??n print fmt.Println(content)
#El contenido de la impresi??n puede ser:
# fmt.Println(x, ???String???)
# fmt.Println(???String???, y)
# fmt.Println(???String???, y, ???String???)
# fmt.Println("String", "String", y)
def p_impresion_content(p):
  '''impresion_content : impresion_type
  | impresion_type COMMA impresion_type
  | impresion_type COMMA impresion_type COMMA impresion_content'''

#Para reducir el n??mero de operaciones OR en impresion_content
def p_impresion_type(p):
  '''impresion_type : VARIABLE
  | STR'''

#ESTRUCTURAS DE CONTROL:Tienen reglas sint??cticas para selecci??n y repetici??n. Se pueden anidar, agregar al cuerpo otras reglas.

#EXTRA

def p_error(p):
  if p:
    str = f"Error de sintaxis - Token: {p.type}, L??nea: {p.lineno}, Col: {p.lexpos}"
    parser.errok()
    listaerr.append(str)

def obtenerErrores():
  return listaerr

# Build the parser
parser = yacc.yacc()
parser.lineno = 0
#Andrea
def validaRegla(s):
  result = parser.parse(s, debug=False)
  print(result)
  return str(result)