from tkinter import *
from tkinter import filedialog, messagebox
import random
import datetime


precios_comida = [1.32, 1.65, 2.31, 3.22, 1.22, 1.99, 2.05, 2.65]
precios_bebida = [0.25, 0.99, 1.21, 1.54, 1.08, 1.10, 2.00, 1.58]
precios_postres = [1.54, 1.68, 1.32, 1.97, 2.55, 2.14, 1.94, 1.74]

operador = ''

def click_boton(numero):
    global operador
    operador = operador + numero
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(END, operador)


def borrar():
    global operador
    operador = ''
    visor_calculadora.delete(0, END)


def obtener_resultado():
    global operador
    resultado = str(eval(operador))
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(0, resultado)
    operador = resultado


def revisar_check():
     x= 0
     for c in cuadros_comida:
         if variables_comida[x].get() == 1:
             cuadros_comida[x].config(state=NORMAL)
             if cuadros_comida[x].get() == '0':
                cuadros_comida[x].delete(0, END)
             cuadros_comida[x].focus()
         else:
             cuadros_comida[x].config(state=DISABLED)
             texto_comida[x].set('0')

         x += 1

     x= 0
     for c in cuadros_bebida:
         if variables_bebida[x].get() == 1:
             cuadros_bebida[x].config(state=NORMAL)
             if cuadros_bebida[x].get() == '0':
                cuadros_bebida[x].delete(0, END)
             cuadros_bebida[x].focus()
         else:
             cuadros_bebida[x].config(state=DISABLED)
             texto_bebida[x].set('0')
             
         x += 1

     x= 0
     for c in cuadros_postre:
         if variables_postre[x].get() == 1:
             cuadros_postre[x].config(state=NORMAL)
             if cuadros_postre[x].get() == '0':
                cuadros_postre[x].delete(0, END)
             cuadros_postre[x].focus()
         else:
             cuadros_postre[x].config(state=DISABLED)
             texto_postre[x].set('0')
             
         x += 1


def total():
    subtotal_comida = 0
    p = 0
    for cantidad in texto_comida:
        subtotal_comida = subtotal_comida + (float(cantidad.get()) * precios_comida[p])
        p += 1

    subtotal_bebida = 0
    p = 0
    for cantidad in texto_bebida:
        subtotal_bebida = subtotal_bebida + (float(cantidad.get()) * precios_bebida[p])
        p += 1

    subtotal_postre = 0
    p = 0
    for cantidad in texto_postre:
        subtotal_postre = subtotal_postre + (float(cantidad.get()) * precios_postres[p])
        p += 1


    sub_total = subtotal_comida + subtotal_bebida + subtotal_postre
    impuestos = sub_total * 0.07
    total = sub_total + impuestos

    var_costo_comida.set(f'$ {round(subtotal_comida, 2)}')
    var_costo_bebida.set(f'$ {round(subtotal_bebida, 2)}')
    var_costo_postre.set(f'$ {round(subtotal_postre, 2)}')
    var_subtotal.set(f'$ {round(sub_total, 2)}')
    var_impuesto.set(f'$ {round(impuestos, 2)}')
    var_total.set(f'$ {round(total, 2)}')


def recibo():
    texto_recibo.delete(1.0, END)
    numero_recibo = f'N# - {random.randint(1000, 9999)}'
    fecha = datetime.datetime.now()
    fecha_recibo = f'{fecha.day}/{fecha.month}/{fecha.year} - {fecha.hour}:{fecha.minute}'
    texto_recibo.insert(END, f'Datos:\t{numero_recibo}\t\t{fecha_recibo}\n')
    texto_recibo.insert(END, '*' * 69 + '\n')
    texto_recibo.insert(END, 'Items\t\tCant.\tCosto Items\n')
    texto_recibo.insert(END, '-' * 69 + '\n') 

    x = 0
    for comida in texto_comida:
        if comida.get() != '0':
            texto_recibo.insert(END, f'{lista_comidas[x]}\t\t{comida.get()}\t$ {int(comida.get()) * precios_comida[x]}\n')

        x += 1

    x = 0
    for bebida in texto_bebida:
        if bebida.get() != '0':
            texto_recibo.insert(END, f'{lista_bebidas[x]}\t\t{bebida.get()}\t$ {int(bebida.get()) * precios_bebida[x]}\n')

        x += 1

    x = 0
    for postre in texto_postre:
        if postre.get() != '0':
            texto_recibo.insert(END, f'{lista_postres[x]}\t\t{postre.get()}\t$ {int(postre.get()) * precios_postres[x]}\n')

        x += 1

    texto_recibo.insert(END, '-' * 69 + '\n')
    texto_recibo.insert(END, f'Costo de la comida: \t\t\t{var_costo_comida.get()}\n')
    texto_recibo.insert(END, f'Costo de las bebidas: \t\t\t{var_costo_bebida.get()}\n')
    texto_recibo.insert(END, f'Costo de los postres: \t\t\t{var_costo_postre.get()}\n')
    texto_recibo.insert(END, '-' * 69 + '\n')
    texto_recibo.insert(END, f'Subtotal: \t\t\t{var_subtotal.get()}\n')
    texto_recibo.insert(END, f'Impuestos: \t\t\t{var_impuesto.get()}\n')
    texto_recibo.insert(END, f'Total: \t\t\t{var_total .get()}\n')
    texto_recibo.insert(END, '*' * 69 + '\n')
    texto_recibo.insert(END, 'Lo esperamos pronto')


def guardar():
    info_recibo = texto_recibo.get(1.0, END)
    archivo = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    archivo.write(info_recibo)
    archivo.close()
    messagebox.showinfo('Informacion', 'Su recibo ha sido guardado')


def resetear():
    texto_recibo.delete(0.1, END)

    for texto in texto_comida:
        texto.set('0')
    for texto in texto_bebida:
        texto.set('0')
    for texto in texto_postre:
        texto.set('0')

    for cuadro in cuadros_comida:
        cuadro.config(state=DISABLED)
    for cuadro in cuadros_bebida:
        cuadro.config(state=DISABLED)
    for cuadro in cuadros_postre:
        cuadro.config(state=DISABLED)

    for v in variables_comida:
        v.set(0)
    for v in variables_bebida:
        v.set(0)
    for v in variables_postre:
        v.set(0)

    var_costo_comida.set('')
    var_costo_bebida.set('')
    var_costo_postre.set('')
    var_subtotal.set('')
    var_impuesto.set('')
    var_total.set('')
    

# iniciar tkinder
aplicacion = Tk()

# tamaño de la ventana
aplicacion.geometry('1045x640+0+0')

# evitar cambiar tamaño de la ventana
aplicacion.resizable(0, 0)

# titulo
aplicacion.title('Mi Restaurante - Sistema de Facturación')

# color de fondo RGB (222, 184, 135)
aplicacion.config(bg='burlywood')

# panel superior
panel_superior = Frame(aplicacion, 
                       bd = 1, 
                       relief = FLAT)

panel_superior.pack(side = TOP)

# etiqueta titulo
etiqueta_titulo = Label(panel_superior, 
                        text='Sistema de Facturación', 
                        fg='azure4', 
                        font=('Dosis', 58), 
                        bg='burlywood', 
                        width= '27')

etiqueta_titulo.grid(row=0, column=0)

# panel izquierdo
panel_izquierdo = Frame(aplicacion, 
                        bd=1, 
                        relief=FLAT)

panel_izquierdo.pack(side=LEFT)

# panel costos
panel_costos = Frame(panel_izquierdo, 
                     bd=1, 
                     relief=FLAT, 
                     bg='azure4', 
                     padx=50)

panel_costos.pack(side=BOTTOM)

# panel comidas
panel_comidas = LabelFrame(panel_izquierdo, 
                           text='Comida', 
                           font=('Dosis', 19, 'bold'), 
                           bd=1, 
                           relief=FLAT, 
                           fg='azure4')

panel_comidas.pack(side=LEFT)

# panel bebidas
panel_bebidas = LabelFrame(panel_izquierdo, 
                           text='Bebidas', 
                           font=('Dosis', 19, 'bold'), 
                           bd=1, 
                           relief=FLAT, 
                           fg='azure4')

panel_bebidas.pack(side=LEFT)

# panel postres
panel_postres = LabelFrame(panel_izquierdo, 
                           text='Postres', 
                           font=('Dosis', 19, 'bold'), 
                           bd=1, 
                           relief=FLAT, 
                           fg='azure4')

panel_postres.pack(side=LEFT)

# panel derecha
panel_derecha = Frame(aplicacion, 
                      bd=1, 
                      relief=FLAT)

panel_derecha.pack(side=RIGHT)

# panel calculadora
panel_calculadora = Frame(panel_derecha, 
                          bd=1, 
                          relief=FLAT, 
                          bg='burlywood')

panel_calculadora.pack()

# panel recibo
panel_recibo = Frame(panel_derecha, 
                     bd=1, 
                     relief=FLAT, 
                     bg='burlywood')

panel_recibo.pack()

# panel botones
panel_botones = Frame(panel_derecha, 
                      bd=1, 
                      relief=FLAT, 
                      bg='burlywood')

panel_botones.pack()

# lista de productos
lista_comidas = ['Pollo', 'Cordero', 'Salmon', 'Merluza', 'Kebab', 'Pizza1', 'Pizza2', 'Pizza3']
lista_bebidas = ['Agua', 'Soda', 'Jugo', 'Cola', 'Vino tipo1', 'Vino2', 'Cerveza1', 'Cerveza2']
lista_postres = ['Helado', 'Frutas', 'Brownies', 'Flan', 'Mousse', 'Pastel1', 'Paste2', 'Pastel3']

# generar items comida
variables_comida = []
cuadros_comida = []
texto_comida = []

contador = 0

for comida in lista_comidas:

    # crear checkbutton
    variables_comida.append('')
    variables_comida[contador] = IntVar()
    comida = Checkbutton(panel_comidas, 
                         text=comida.title(), 
                         font=('Dosis', 19, 'bold'), 
                         onvalue=1, 
                         offvalue=0, 
                         variable=variables_comida[contador],
                         command= lambda : revisar_check())

    comida.grid(row=contador, 
                column=0, 
                sticky=W)

    # crear los cuadros de entrada
    cuadros_comida.append('')
    texto_comida.append('')
    texto_comida[contador] = StringVar()
    texto_comida[contador].set(0)
    cuadros_comida[contador] = Entry(panel_comidas, 
                                     font=('Dosis', 18, 'bold'), 
                                     bd=1, width=6, 
                                     state=DISABLED, 
                                     textvariable=texto_comida[contador])
    
    cuadros_comida[contador].grid(row=contador, 
                                  column=1)

    contador += 1


# generar items bebida
variables_bebida = []
cuadros_bebida = []
texto_bebida = []

contador = 0

for bebida in lista_bebidas:

    # crear checkbutton
    variables_bebida.append('')
    variables_bebida[contador] = IntVar()
    bebida = Checkbutton(panel_bebidas, 
                         text=bebida.title(), 
                         font=('Dosis', 19, 'bold'), 
                         onvalue=1, 
                         offvalue=0, 
                         variable=variables_bebida[contador],
                         command= lambda : revisar_check())

    bebida.grid(row=contador, 
                column=0, 
                sticky=W)

    # crear los cuadros de entrada
    cuadros_bebida.append('')
    texto_bebida.append('')
    texto_bebida[contador] = StringVar()
    texto_bebida[contador].set(0)
    cuadros_bebida[contador] = Entry(panel_bebidas, 
                                     font=('Dosis', 18, 'bold'), 
                                     bd=1, width=6, 
                                     state=DISABLED, 
                                     textvariable=texto_bebida[contador])
    cuadros_bebida[contador].grid(row=contador, 
                                  column=1)

    contador += 1


# generar items postre
variables_postre = []
cuadros_postre = []
texto_postre = []

contador = 0

for postre in lista_postres:

    # crear checkbutton
    variables_postre.append('')
    variables_postre[contador] = IntVar()
    postre = Checkbutton(panel_postres, 
                         text=postre.title(), 
                         font=('Dosis', 19, 'bold'), 
                         onvalue=1, 
                         offvalue=0, 
                         variable=variables_postre[contador],
                         command= lambda : revisar_check())

    postre.grid(row=contador, 
                column=0, 
                sticky=W)
    
    # crear los cuadros de entrada
    cuadros_postre.append('')
    texto_postre.append('')
    texto_postre[contador] = StringVar()
    texto_postre[contador].set(0)
    cuadros_postre[contador] = Entry(panel_postres, 
                                     font=('Dosis', 18, 'bold'), 
                                     bd=1, width=6, 
                                     state=DISABLED, 
                                     textvariable=texto_postre[contador])
    
    cuadros_postre[contador].grid(row=contador, 
                                  column=1)

    contador += 1

# variables
var_costo_comida = StringVar()
var_costo_bebida = StringVar()
var_costo_postre = StringVar()
var_subtotal = StringVar()
var_impuesto = StringVar()
var_total = StringVar()

# etiquetas de costo y los campos de entrada
etiqueta_costo_comida = Label(panel_costos, 
                              text='Costo comida', 
                              font=('Dosis', 12, 'bold'), 
                              bg='azure4', 
                              fg='white')

etiqueta_costo_comida.grid(row=0, 
                           column=0)

texto_costo_comida = Entry(panel_costos, 
                           font=('Dosis', 12, 'bold'), 
                           bd=1, width=10, 
                           state='readonly', 
                           textvariable=var_costo_comida)

texto_costo_comida.grid(row=0, 
                        column=1, 
                        padx=41)

etiqueta_costo_bebida = Label(panel_costos, 
                              text='Costo bebida', 
                              font=('Dosis', 12, 'bold'), 
                              bg='azure4', 
                              fg='white')

etiqueta_costo_bebida.grid(row=1, 
                           column=0)

texto_costo_bebida = Entry(panel_costos, 
                           font=('Dosis', 12, 'bold'), 
                           bd=1, width=10, 
                           state='readonly', 
                           textvariable=var_costo_bebida)

texto_costo_bebida.grid(row=1, 
                        column=1, 
                        padx=41)

etiqueta_costo_postre = Label(panel_costos, 
                              text='Costo postre', 
                              font=('Dosis', 12, 'bold'), 
                              bg='azure4', 
                              fg='white')

etiqueta_costo_postre.grid(row=2, 
                           column=0)

texto_costo_postre = Entry(panel_costos, 
                           font=('Dosis', 12, 'bold'), 
                           bd=1, width=10, 
                           state='readonly', 
                           textvariable=var_costo_postre)

texto_costo_postre.grid(row=2, 
                        column=1, 
                        padx=41)

etiqueta_costo_subtotal = Label(panel_costos, 
                                text='Subtotal', 
                                font=('Dosis', 12, 'bold'), 
                                bg='azure4', 
                                fg='white')

etiqueta_costo_subtotal.grid(row=0, 
                             column=2)

texto_costo_subtotal = Entry(panel_costos, 
                             font=('Dosis', 12, 'bold'), 
                             bd=1, width=10, 
                             state='readonly', 
                             textvariable=var_subtotal)

texto_costo_subtotal.grid(row=0, 
                          column=3, 
                          padx=41)

etiqueta_costo_impuestos = Label(panel_costos, 
                                 text='Impuestos', 
                                 font=('Dosis', 12, 'bold'), 
                                 bg='azure4', 
                                 fg='white')

etiqueta_costo_impuestos.grid(row=1, 
                              column=2)

texto_costo_impuestos = Entry(panel_costos, 
                              font=('Dosis', 12, 'bold'), 
                              bd=1, width=10, 
                              state='readonly', 
                              textvariable=var_impuesto)

texto_costo_impuestos.grid(row=1, 
                           column=3, 
                           padx=41)

etiqueta_costo_total = Label(panel_costos, 
                             text='Total', 
                             font=('Dosis', 12, 'bold'), 
                             bg='azure4', 
                             fg='white')

etiqueta_costo_total.grid(row=2, 
                          column=2)

texto_costo_total = Entry(panel_costos, 
                          font=('Dosis', 12, 'bold'), 
                          bd=1, 
                          width=10, 
                          state='readonly', 
                          textvariable=var_total)

texto_costo_total.grid(row=2, 
                       column=3, 
                       padx=41)

# Botones
botones = ['Total', 'Recibo', 'Guardar', 'Resetear']
botones_creados = []

columnas = 0
for boton in botones:
    boton = Button(panel_botones, 
                   text=boton.title(), 
                   font=('Dosis', 14, 'bold'), 
                   fg='black', 
                   bg='white', 
                   bd=1, 
                   width=7)
    
    botones_creados.append(boton)

    boton.grid(row=0, 
               column=columnas)
    
    columnas += 1

botones_creados[0].config(command= lambda: total())
botones_creados[1].config(command= lambda: recibo())
botones_creados[2].config(command= lambda: guardar())
botones_creados[3].config(command= lambda: resetear ())

# area de recibo
texto_recibo = Text(panel_recibo, 
                    font=('Dosis', 12, 'bold'), 
                    bd=1, 
                    width=45, 
                    height=10)

texto_recibo.grid(row=0, 
                  column=0)

# calculadora
visor_calculadora = Entry(panel_calculadora, 
                          font=('Dosis', 16, 'bold'), 
                          width=36, 
                          bd=1)

visor_calculadora.grid(row=0, 
                       column=0, 
                       columnspan=4)

botones_calculadora = ['7', '8', '9', '+', 
                       '4', '5', '6', '-', 
                       '1', '2', '3', 'x', 
                       '=', 'CLR', '0', '/']

botones_guardados = [ ]

fila = 1
columna = 0
for boton in botones_calculadora:
    boton = Button(panel_calculadora, 
                   text=boton.title(), 
                   font=('Dosis', 16, 'bold'), 
                   fg='black', 
                   bg='white', 
                   bd=1, 
                   width=6)

    boton.grid(row=fila, 
               column=columna)

    botones_guardados.append(boton)
    
    if columna == 3:
        fila += 1
    
    columna += 1

    if columna == 4:
        columna = 0

botones_guardados[0].config(command=lambda : click_boton('7'))
botones_guardados[1].config(command=lambda : click_boton('8'))
botones_guardados[2].config(command=lambda : click_boton('9'))
botones_guardados[3].config(command=lambda : click_boton('+'))
botones_guardados[4].config(command=lambda : click_boton('4'))
botones_guardados[5].config(command=lambda : click_boton('5'))
botones_guardados[6].config(command=lambda : click_boton('6'))
botones_guardados[7].config(command=lambda : click_boton('-'))
botones_guardados[8].config(command=lambda : click_boton('1'))
botones_guardados[9].config(command=lambda : click_boton('2'))
botones_guardados[10].config(command=lambda : click_boton('3'))
botones_guardados[11].config(command=lambda : click_boton('*'))
botones_guardados[12].config(command=lambda : obtener_resultado())
botones_guardados[13].config(command=lambda : borrar())
botones_guardados[14].config(command=lambda : click_boton('0'))
botones_guardados[15].config(command=lambda : click_boton('/'))


# evitar que la ventana se cierre
aplicacion.mainloop()