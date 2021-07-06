from tkinter import *
from tkinter import ttk

def loadbar(m):
    cont = 0
    etapas = m/100

    while cont < etapas:
        cont = cont+1
        i = 0
        while i < 1000000:
            i = i + 1
        varBarra.set(cont)
        app.update()

app = Tk()
app.title("Aula 79")
app.geometry("300x300")

varBarra = DoubleVar()
varBarra.set(0)

pb = ttk.Progressbar(app, variable=varBarra, maximum=100)
pb.place(x=0, y=0, width=300)

btn = Button(app, text="Iniciar barra", command=lambda:loadbar(10000))
btn.place(x=10, y=40)

app.mainloop()