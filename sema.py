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
