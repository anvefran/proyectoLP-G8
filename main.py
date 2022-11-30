import tkinter as tk
from tkinter import scrolledtext
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
from PIL import ImageTk, Image

#Gabriel
def select_file():
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)

    showinfo(
        title='Selected File',
        message=filename
    )

    abrir_archivo(filename)

def abrir_archivo(nomarch):
    file = open(nomarch,'r')
    global datos_parse
    datos_parse = file.read()
    file.close()
    file = open(nomarch,'r')
    text_area.delete('1.0',tk.END)
    for line in file:
        text_area.insert(tk.INSERT, line)
    showinfo(title="Importacion correcta!",message="Su codigo fuente ha sido agregado correctamente.")
    #datos_parse = file.read() #Para el analizador sintatcico
    text_arear.config(state='normal')
    text_arear.delete('1.0',tk.END)
    write_result("Codigo cargado y listo para analizar.")
    text_arear.config(state='disabled')

def borrar_contenido():
    text_area.delete('1.0',tk.END)
    text_arear.config(state='normal')
    text_arear.delete('1.0',tk.END)
    text_arear.config(state='disabled')
    global ingreso
    ingreso = ""
    global datos_parse
    datos_parse = ""


#Guarda el contenido del textbox en un string
def guardar_contenido():
    global ingreso
    ingreso = text_area.get('1.0',tk.END)
    if ingreso.strip() == "":
        showinfo(
        title='Error!',message="No se ha podido cargar el codigo. Revisa tu entrada!")
        return
    fileaux = open("fuente.txt","w")
    for elem in ingreso:
        fileaux.write(elem)
    #print(ingreso)
    fileaux.close()
    abrir_archivo("fuente.txt")
    text_arear.config(state='normal')
    text_arear.delete('1.0',tk.END)
    write_result("Codigo cargado y listo para analizar.")
    text_arear.config(state='disabled')

#Eduardo
#Escribe los resultados en el area de resultados
def write_result(string):
    text_arear.config(state='normal')
    text_arear.insert(tk.INSERT, string)
    text_arear.config(state='disabled')

def lexer():
    text_arear.config(state='normal')
    text_arear.delete('1.0',tk.END)
    text_arear.config(state='disabled')
    import lexico as lx
    lx.lexer.input(datos_parse)
    ltok = lx.getTokens(lx.lexer)
    write_result("Tokens:\n")
    write_result(ltok)