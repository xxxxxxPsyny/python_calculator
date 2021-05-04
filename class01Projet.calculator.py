#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from tkinter import *

from tkinter import messagebox

calc = Tk()
calc.title("Calculadora - DataScience with Python")
calc.geometry("400x300")
calc.resizable(width = False, height = False)
calc.configure(background="#dde")
l = Label(calc, text = "Calculadora Python")
l.place(x=200, y=25, anchor="center")
l.config(font =("Comic Sams", 14))

def calculate(dowhat):   
    num1 = vvalue1.get()
    num2 = vvalue2.get()
    operation = dowhat
    if operation == 1:
        result = float(num1) + float(num2)
    elif operation == 2:
        result = float(num1) - float(num2)
    elif operation == 3:
        result = float(num1) * float(num2)
    elif operation == 4:
        if num2 == "0": messagebox.showerror('Cabaço!', 'O divisor deve ser >= 0 :D')
        else:
            result = float(num1) / float(num2)
    elif operation == 5:
        result = float(num1) ** float(num2)
    print(result)
    
    global rl1    
    rl1 = Label(calc, text = "Resultado")
    rl1.place(x=200, y=200, anchor="center")
    rl1.config(font =("Comic Sams", 12))

    global rl2    
    rl2 = Label(calc, text = result)
    rl2.place(x=200, y=230, anchor="center")
    rl2.config(font =("Comic Sams", 20))

def clear_label():
    rl2.config(text = "")
    
Label(calc, text = "Digite um valor", foreground = "#009", anchor = W).place(x = 10, y = 50, width = 100, height = 20)
vvalue1 = Entry(calc)
vvalue1.place(x = 10, y = 70, width = 200, height = 20)

Label(calc, text= "Digitel um valor", foreground = "#009", anchor = W).place(x = 10, y = 100, width = 100, height = 20)
vvalue2 = Entry(calc)
vvalue2.place(x = 10, y = 120, width = 200, height = 20)


Label(calc, text= "Operação", foreground = "#009", anchor = W).place(x = 260, y = 50, width = 100, height = 20)

B1 = Button(calc, text = "Soma", command = lambda: calculate(1))
B1.place(x = 250,y = 80)

B2 = Button(calc, text = "Subtração", command = lambda: calculate(2))
B2.place(x = 310,y = 80)

B3 = Button(calc, text = "Multiplicação", command = lambda: calculate(3))
B3.place(x = 240,y = 110)

B4 = Button(calc, text = "Divisão", command = lambda: calculate(4))
B4.place(x = 330,y = 110)

B5 = Button(calc, text = "Potência", command = lambda: calculate(5))
B5.place(x = 285,y = 140)

B6 = Button(calc, text = "Limpar Resultados", command = clear_label)
B6.place(x=200, y=280, anchor="center")

calc.mainloop()

