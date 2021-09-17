from tkinter import *
from tkinter import messagebox as MessageBox

#Incio Configuracion Parte Grafica Campos
ventana = Tk()
ventana.title('Calculadora')
txt1 = Label(ventana, text='Seleccione la operacion que desea realizar')
txt1.grid(column=0, row=0)
txt1.place(x=320, y=10, anchor="center")
txt1['bg'] = '#4785D0'
txtnum1 = Label(ventana, text="Ingrese el primer valor")
txtnum1.grid(column=0, row=0)
txtnum1.place(x=65, y=40, anchor="center")
txtnum1['bg'] = '#4785D0'
campo1 = Entry(ventana, width=30)
campo1.grid(column=0, row=0)
campo1.place(x=100, y=60, anchor="center")
txtnum2 = Label(ventana, text="Ingrese el segundo valor")
txtnum2.grid(column=0, row=0)
txtnum2.place(x=70, y=80, anchor="center")
txtnum2['bg'] = '#4785D0'
campo2 = Entry(ventana, width=30)
campo2.grid(column=0, row=0)
campo2.place(x=100, y=100, anchor="center")
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


#Calculo de factorizacion por formula general Ejemplo: x^2+3x-4 || Factoring calculation by general formula Example: x^2+3x-4
def Factorizar(): 
    if campo1.get() != '':
        MessageBox.showinfo("Alerta", "El calculo de la factorizacion solo toma el valor del primer campo")
        ecuacion = campo1.get()
        valor1 = ecuacion.split('x^2')

        if valor1[0] == '':
            a = 1
        else:
            a = int(valor1[0])

        cadena2 = valor1[1].split('x')

        if cadena2[0].count('+') > 0:
            caracter = '+'
            valor2 = cadena2[0].split(caracter) 
            b = float(valor2[1])
        elif cadena2[0].count('-') > 0:
            valor2 = cadena2[0]
            b = float(valor2)
        else:
            caracter = ''
        
        if cadena2[1].count('+') > 0:
            caracter1 = '+'
            valor3 = cadena2[1].split(caracter1)
            c = float(valor3[1])
        elif cadena2[1].count('-') > 0:
            valor3 = cadena2[1]            
            c = float(valor3)
        else:
            caracter1 = ''

        xsub1 = -b + pow(((b*b)-4*a*c),0.5)
        xsub2 = -b - pow(((b*b)-4*a*c),0.5)

        x1 = xsub1 / (2*a)
        x2 = xsub2 / (2*a)

        print(x1)
        print(x2)

        if float(x1) == 0:
            igualacion = 0
        elif float(x1) < 0:
            igualacion = x1 * -1 
        else:
            igualacion = '-'+str(x1)

        if float(x2) == 0:
            igualacion2 = 0
        elif float(x2) < 0:
            igualacion2 = x2 * -1
        else:
            igualacion2 = '-'+str(x2)  
        
        if float(igualacion) > 0 and float(igualacion2) < 0:
            resultado = '(x+'+str(igualacion)+') (x'+str(igualacion2)+')'
        elif float(igualacion) < 0 and float(igualacion2) > 0:
            resultado = '(x'+str(igualacion)+') (x+'+str(igualacion2)+')'
        elif float(igualacion) > 0 and float(igualacion2) > 0:
            resultado = '(x+'+str(igualacion)+') (x+'+str(igualacion2)+')'
        elif float(igualacion) < 0 and float(igualacion2) < 0:
            resultado = '(x+'+str(igualacion)+') (x+'+str(igualacion2)+')'

        txtnum3['text'] = "Resultado: "+resultado

def Limpiar():
    campo1.delete(0, END)
    campo2.delete(0, END)
    txtnum3['text'] = "Resultado: 0"

#Fin Funciones

#Inicio Botones
btnsum = Button(ventana, text="SUMAR", command=Suma)
btnsum.grid(column=0, row=0)
btnsum.place(x=505, y=60, anchor="center")
btnres = Button(ventana, text="RESTAR", command=Resta)
btnres.grid(column=0, row=0)
btnres.place(x=505, y=90, anchor="center")
btndiv = Button(ventana, text="DIVIDIR", command=Dividir)
btndiv.grid(column=0, row=0)
btndiv.place(x=505, y=120, anchor="center")
btnmul = Button(ventana, text="MULTIPLICAR", command=Multiplica)
btnmul.grid(column=0, row=0)
btnmul.place(x=505, y=150, anchor="center")
btnraiz = Button(ventana, text="RAIZ", command=Raiz)
btnraiz.grid(column=0, row=0)
btnraiz.place(x=505, y=180, anchor="center")
btnfac = Button(ventana, text="FACTORIZAR", command=Factorizar)
btnfac.grid(column=0, row=0)
btnfac.place(x=505, y=210, anchor="center")
btnclear = Button(ventana, text="LIMPIAR", command=Limpiar)
btnclear.grid(column=0, row=0)
btnclear.place(x=505, y=240, anchor="center")
#Fin Botones

#Inicio Parte Grafica Resultado y Ventana
txtnum3 = Label(ventana, text="Resultado: 0")
txtnum3.grid(column=0, row=0)
txtnum3.place(x=200, y=228, anchor="center")
txtnum3.config(font=("Arial",18))
txtnum3['bg'] = '#4785D0'
ventana.geometry('600x300')
ventana['bg'] = '#4785D0'
ventana.mainloop()
#Fin Parte Grafica Resultado y Ventana

#Daniel Hernandez 2021