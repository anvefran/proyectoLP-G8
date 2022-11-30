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