from tkinter import *

app = Tk()
app.title("Aula 77")
app.geometry("300x300")

def showValor():
    print("Valor: "+str(sb_valores1.get()))

sb_valores1 = Spinbox(app, from_=1, to=10)
sb_valores1.pack()

btn1 = Button(app, text="Defina um valor", command=showValor)
btn1.pack()

sb_valores2 = Spinbox(app, values=(1,2,3,4,5))
sb_valores2.pack()

app.mainloop()