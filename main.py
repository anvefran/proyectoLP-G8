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