from tkinter import *
from tkinter import messagebox

import database as db
from estilos import *
def form_editar_clientes(id):

    # variables de ingreso
    input_nombre = st()
    input_apellido = stringVar()
    ipunt_dni = stringhVar()
    input_telefono = stringVar()