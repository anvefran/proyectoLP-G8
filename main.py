import ply.yacc as yacc
import sys
from lexico import tokens
from datetime import datetime

with open('log.txt', 'a') as sys.stdout:
  #CUERPO (Andrea-Gabriel-Eduardo)
  def p_cuerpo(p):
    '''cuerpo : asignacion
    | inicio
    | operacion
    | comparacion
    | slice
    | sliceMethods
    | impresion
    | conditional_structure
    | arrays
  	| maps
    | mapelem
    | input
    | impresionln
    | funcion
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
    | VAR VARIABLE datatype IGUAL valor
    | VAR VARIABLE IGUAL valor'''
  
  
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
    | STR '''
  
  
  def p_numero(p):
    '''numero : ENTERO
    | FLOAT'''
  
  
  #EXPRESIONES: operaciones y comparaciones - Andrea
  def p_operacion(p):
    '''operacion : VARIABLE operadorOp VARIABLE
    | numero operadorOp numero
    | VARIABLE incDec 
    | VARIABLE operadorOp valor
    | valor operadorOp VARIABLE
    | VARIABLE PLUS IGUAL valor
    | VARIABLE PLUS IGUAL VARIABLE'''
  
  
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
    | valor operadorCmp valor
    | valor operadorCmp VARIABLE
    | VARIABLE operadorCmp valor
    | operacion operadorCmp valor
    | operacion operadorCmp operacion'''
  
  
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
  
  
  #Funciones - Eduardo Salavarría
  #1er caso: funciones sin argumentos, sin retornos "func variable()(){body}"
  #2do caso: con retorno sin argumentos
  #3er caso: sin retorno con n argumentos
  #4to caso: con retorno, con argumentos
  #Psdt: en el mismo sintáctico se valida que la función retorne un elemento en caso que haya sido declarado como función con elementos de retorno
  
  
  def p_funcion(p):
    '''funcion : FUNCTION VARIABLE LPAREN RPAREN LPAREN RPAREN LEFTKEY cuerpo RIGHTKEY
    | FUNCTION VARIABLE  LPAREN  RPAREN LPAREN freturns RPAREN LEFTKEY fbody_wreturn RIGHTKEY
    | FUNCTION VARIABLE  LPAREN  farguments RPAREN LPAREN RPAREN LEFTKEY cuerpo RIGHTKEY
    | FUNCTION VARIABLE  LPAREN  farguments RPAREN LPAREN freturns RPAREN LEFTKEY fbody_wreturn RIGHTKEY'''
  
  
  #funcion que apoya a "funcion"  declara funciones single-argument y multiple-argument
  def p_farguments(p):
    '''farguments : VARIABLE datatype
    | VARIABLE datatype COMMA farguments'''
  
  
  #función de apoyo a "funcion" permite que las funciones tenga uno o múltiple retornos
  def p_freturns(p):
    '''freturns : datatype
    | datatype COMMA freturns'''
  
  
  #cuerpo de la función con retorno (debe tener una linea return a, b, ...)
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
  #Método para mostrar en pantalla (Coloca un salto de línea al final de la cadena de caracteres)
  def p_impresionln(p):
    '''impresionln : FMT DOT PRINTLN LPAREN impresion_content RPAREN'''
  
  
  #Contiene el contenido de la función print fmt.Println(content)
  #El contenido de la impresión puede ser:
  # fmt.Println(x, “String”)
  # fmt.Println(“String”, y)
  # fmt.Println(“String”, y, “String”)
  # fmt.Println("String", "String", y)
  def p_impresion_content(p):
    '''impresion_content : impresion_type
    | impresion_type COMMA impresion_type
    | impresion_type COMMA impresion_type COMMA impresion_content'''
  
  
  #Para reducir el número de operaciones OR en impresion_content
  def p_impresion_type(p):
    '''impresion_type : VARIABLE
    | STR'''
  
  
  #ESTRUCTURAS DE CONTROL:Tienen reglas sintácticas para selección y repetición. Se pueden anidar, agregar al cuerpo otras reglas.
  
  
  #EXTRA
  
  def p_error(p):
    if p:
      print(
        f"Error de sintaxis - Token: {p.type}, Línea: {p.lineno}, Col: {p.lexpos}"
      )
      parser.errok()
  
  # Build the parser
  parser = yacc.yacc()
  
  #Andrea
  def validaRegla(s):
    result = parser.parse(s)
    print(result)
    return str(result)
  
  
  file = open("source.txt")
  
  for line in file:
    try:
      s = line
    except EOFError:
      break
    if not s: continue
    print(line)
    validaRegla(s)
    print(datetime.now())