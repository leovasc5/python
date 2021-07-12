from tkinter import *
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import os

def convert(mm):
    return mm/0.352777    
    
def criarPDF():
    try:
        cnv = canvas.Canvas(os.path.dirname(__file__)+"\\exemplo.pdf", pagesize=A4)
        cnv.setTitle("Arquivo de Teste")
        cnv.drawImage(os.path.dirname(__file__)+"\\python.png", convert(15), convert(110), mask="auto")
        cnv.drawString(convert(80), convert(90), "Leonardo Vasconcelos")
        cnv.save()
        print("PDF Criado")
    except:
        print("Erro")

app = Tk()
app.title("Aula 85")
app.geometry("320x350")

btn1 = Button(app, text="Criar PDF", command=criarPDF)
btn1.place(x=60, y=60)

app.mainloop()