from tkinter import *
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import os

def criarPDF():
    cnv = canvas.Canvas(os.path.dirname(__file__)+"\\exemplo.pdf", pagesize=A4)
    cnv.drawString(50, 50, "Leonardo Vasconcelos")
    cnv.save()
    print("PDF Criado")

app = Tk()
app.title("Aula 83")
app.geometry("320x350")

btn1 = Button(app, text="Criar PDF", command=criarPDF)
btn1.place(x=60, y=60)

app.mainloop()