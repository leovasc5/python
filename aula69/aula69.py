from tkinter import *
import os

app = Tk()
app.title("Aula 69")
app.geometry("500x475")

pastaApp = os.path.dirname(__file__)
img = PhotoImage(file=pastaApp+"\\img.png")
lbl1 = Label(app, image=img)
lbl1.place(x=10, y=10)

app.mainloop()