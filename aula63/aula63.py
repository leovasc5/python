from tkinter import *

app = Tk()
app.title("Aula 63")
app.geometry("500x300")
escolhido = ""

def showEsporte():
    if vesporte.get() == "f":
        escolhido = "Futebol"
        print(escolhido)
    elif vesporte.get() == "v" :
        escolhido = "Vôlei" 
        print(escolhido)
    elif vesporte.get() == "b" :
        escolhido = "Basquete"
        print(escolhido)
    else:
        print("Escolha novamente")
        
vesporte = StringVar()

esportes = Label(app, text="Esportes")
esportes.pack()

rb_futebol = Radiobutton(app, text="Futebol", value="f", variable=vesporte)
rb_futebol.pack()

rb_volei = Radiobutton(app, text="Vôlei", value="v", variable=vesporte)
rb_volei.pack()

rb_basquete = Radiobutton(app, text="Basquete", value="b", variable=vesporte)
rb_basquete.pack()

btn_esporte =  Button(app, text="Esporte Selecionado", command=showEsporte)
btn_esporte.pack()

app.mainloop()