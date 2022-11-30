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
  | numero operadorOp masNumeros'''

def p_operacionSTR(p):
  '''operacionSTR : STR operadorOp masSTR'''
def p_masSTR(p):
  '''masSTR : STR
  | VARIABLE
  | STR operadorOp masSTR'''
  
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
  | SWITCH asignacion SEMICOLON VARIABLE LEFTKEY cuerposwitch RIGHTKEY'''

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
  | DEFAULT COLON cuerpo
  | DEFAULT COLON
  '''

def p_cuerposwitch(p):
  '''cuerposwitch : cuerposwitchin
  | cuerposwitchin cuerposwitchin
  | cuerposwitchin cuerposwitchin cuerposwitchin
  '''

def p_forbody(p):
  '''forbody : cuerpo
  | FOR asignacion SEMICOLON comparacion SEMICOLON operacion LEFTKEY cuerpo RIGHTKEY
  '''

#ESTRUCTURAS DE DATOS: reglas sintácticas para declarar estructuras, es posible invocar a sus métodos.
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
