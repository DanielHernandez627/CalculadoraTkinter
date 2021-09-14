from tkinter import *
from tkinter import messagebox as MessageBox

#Incio Configuracion Parte Grafica Campos
ventana = Tk()
ventana.title('Calculadora')
txt1 = Label(ventana, text='Seleccione la operacion que desea realizar')
txt1.grid(column=0, row=0)
txt1.place(x=200, y=10, anchor="center")
txt1['bg'] = '#4785D0'
txtnum1 = Label(ventana, text="Ingrese el primer valor")
txtnum1.grid(column=0, row=0)
txtnum1.place(x=65, y=40, anchor="center")
txtnum1['bg'] = '#4785D0'
campo1 = Entry(ventana, width=20)
campo1.grid(column=0, row=0)
campo1.place(x=65, y=60, anchor="center")
txtnum2 = Label(ventana, text="Ingrese el segundo valor")
txtnum2.grid(column=0, row=0)
txtnum2.place(x=65, y=80, anchor="center")
txtnum2['bg'] = '#4785D0'
campo2 = Entry(ventana, width=20)
campo2.grid(column=0, row=0)
campo2.place(x=65, y=100, anchor="center")
#Fin Configuracion Parte Grafica Campos

#Inicio Funciones


def Suma():
    if campo1.get() != '' and campo2.get() != '':
        n1 = int(campo1.get())
        n2 = int(campo2.get())
    else:
        n1 = 0
        n2 = 0
    resultado = n1 + n2
    txtnum3['text'] = "Resultado: " + str(resultado)


def Resta():
    if campo1.get() != '' and campo2.get() != '':
        n1 = int(campo1.get())
        n2 = int(campo2.get())
    else:
        n1 = 0
        n2 = 0
    resultado = n1 - n2
    txtnum3['text'] = "Resultado: " + str(resultado)


def Multiplica():
    if campo1.get() != '' and campo2.get() != '':
        n1 = int(campo1.get())
        n2 = int(campo2.get())
    else:
        n1 = 0
        n2 = 0
    resultado = n1 * n2
    txtnum3['text'] = "Resultado: " + str(resultado)


def Dividir():
    if campo1.get() != '' and campo2.get() != '':
        n1 = int(campo1.get())
        n2 = int(campo2.get())
        resultado = n1 / n2
    else:
        n1 = 0
        n2 = 0
        resultado = 0
    
    txtnum3['text'] = "Resultado: " + str(resultado)


def Raiz():
    if campo1.get() != '':
        MessageBox.showinfo("Alerta", "El calculo de la raiz solo toma el valor del primer campo")
        n1 = int(campo1.get())
        resultado = pow(n1,0.5)
    else:
        n1 = 0
        resultado = 0
    txtnum3['text'] = "Resultado: " + str(resultado)


def Limpiar():
    campo1.delete(0, END)
    campo2.delete(0, END)
    txtnum3['text'] = "Resultado: 0"

#Fin Funciones

#Inicio Botones
btnsum = Button(ventana, text="SUMAR", command=Suma)
btnsum.grid(column=0, row=0)
btnsum.place(x=300, y=60, anchor="center")
btnres = Button(ventana, text="RESTAR", command=Resta)
btnres.grid(column=0, row=0)
btnres.place(x=300, y=90, anchor="center")
btndiv = Button(ventana, text="DIVIDIR", command=Dividir)
btndiv.grid(column=0, row=0)
btndiv.place(x=300, y=120, anchor="center")
btnmul = Button(ventana, text="MULTIPLICAR", command=Multiplica)
btnmul.grid(column=0, row=0)
btnmul.place(x=300, y=150, anchor="center")
btnraiz = Button(ventana, text="RAIZ", command=Raiz)
btnraiz.grid(column=0, row=0)
btnraiz.place(x=300, y=180, anchor="center")
btnclear = Button(ventana, text="LIMPIAR", command=Limpiar)
btnclear.grid(column=0, row=0)
btnclear.place(x=300, y=210, anchor="center")
#Fin Botones

#Inicio Parte Grafica Resultado y Ventana
txtnum3 = Label(ventana, text="Resultado: 0")
txtnum3.grid(column=0, row=0)
txtnum3.place(x=35, y=128, anchor="center")
txtnum3['bg'] = '#4785D0'
ventana.geometry('400x250')
ventana['bg'] = '#4785D0'
ventana.mainloop()
#Fin Parte Grafica Resultado y Ventana

#Daniel Hernandez 2021