
from tkinter import *
from tkinter import messagebox
def validarInt(num):
    try:
        int(num)
        return True
    except ValueError:
        return False

        
def calcular():
   # k = validarInt(num1)
    #if k==True:
      
    k=num1.get()/9
    a=(num2.get()-k)/2
    b=(num2.get()+k)/2
    var= str(int(b)) + str(int(a))
    return resultado.set(var)
    
def limpiar():
    clear=""
    return num1.set(clear),num2.set(clear),resultado.set(clear)
def Ingles():
    ventana.withdraw()

    ventana2 = Toplevel() 
    ventana2.title("Guesser guess")
    ventana2.geometry("550x300")
    def calcular():
    
        k=num1.get()/9
        a=(num2.get()-k)/2
        b=(num2.get()+k)/2
        var= str(int(b)) + str(int(a))
        return resultado.set(var)
    
    def limpiar():
        clear=""
        return num1.set(clear),num2.set(clear),resultado.set(clear)
    et1=Label(ventana2,text="1-Think of a 2-digit number that does not repeat ")
    et1.place(x=20,y=0) 

    ej1=Label(ventana2,text="Ej  25 - 52 = -27 ",bg="lightblue")
    ej1.place(x=300,y=40)

    et2=Label(ventana2,text="2- Reverse the number thought") 
    et2.place(x=20,y=30)

    et3=Label(ventana2,text="3-Subtract the number thought with the inverted ")
    et3.place(x=20,y=60)

    num1=IntVar()

    et4=Label(ventana2,text="Enter the result in the box of the subtraction considering sign")
    et4.place(x=20,y=90)
    box1=Entry(ventana2,textvariable=num1,width=10)
    box1.place(x=450,y=90)

    num2=IntVar()

    et5=Label(ventana2,text="Enter the result in the box of the sum of digits of the number thought")
    et5.place(x=20,y=120)

    ej2=Label(ventana2,text="Ej 25 => 2 + 5 = 7 ",bg="lightblue")
    ej2.place(x=100,y=150)

    box2=Entry(ventana2,textvariable=num2,width=10)
    box2.place(x=450,y=120)
    resultado=IntVar()
    btn=Button(ventana2,text="The number you thought of is", command=calcular)
    btn.place(x=200,y=200)
    res=Entry(ventana2,textvariable=resultado,width=10, state="readonly")
    res.place(x=450,y=200)
    limpiar()
    ventana2.mainloop()

    
ventana=Tk()
ventana.title("Adivina Adivinador")
ventana.geometry("550x300")


et1=Label(ventana,text="1- Piense un numero de 2 cifras que no se repita")
et1.place(x=20,y=0) 

ej1=Label(ventana,text="Ej  25 - 52 = -27 ",bg="lightblue")
ej1.place(x=300,y=40)

et2=Label(ventana,text="2- Invierta el Numero pensado") 
et2.place(x=20,y=30)

et3=Label(ventana,text="3- Reste el numero pensado con el invertido")
et3.place(x=20,y=60)

num1=IntVar()

et4=Label(ventana,text="Ingrese el resultado en el box de la resta considerando signo")
et4.place(x=20,y=90)
box1=Entry(ventana,textvariable=num1,width=10)
box1.place(x=450,y=90)

num2=IntVar()

et5=Label(ventana,text="Ingrese el resultado en el box de la suma de digitos del numero pensado")
et5.place(x=20,y=120)

ej2=Label(ventana,text="Ej 25 => 2 + 5 = 7 ",bg="lightblue")
ej2.place(x=100,y=150)

box2=Entry(ventana,textvariable=num2,width=10)
box2.place(x=450,y=120)
resultado=IntVar()
btn=Button(ventana,text="El numero que pensaste es:", command=calcular)
btn.place(x=200,y=200)
res=Entry(ventana,textvariable=resultado,width=10, state="readonly")
res.place(x=450,y=200)

bt_ingles=Button(ventana,text="Cambiar a Ingles",command=Ingles)
bt_ingles.place(x=20,y=250)

limpiar()
ventana.mainloop()