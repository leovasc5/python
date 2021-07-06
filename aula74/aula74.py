from tkinter import *

app = Tk()
app.title("Aula 74")

lb_esportes = LabelFrame(app, text="Esportes", borderwidth=1, relief="solid", labelanchor="n")
lb_esportes.place(x=10, y=10, width=150, height=150)

lbl1 = Label(lb_esportes, text="Hello World!",)
lbl1.pack()

app.mainloop()