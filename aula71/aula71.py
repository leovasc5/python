from tkinter import *

app = Tk()
app.title("Aula 70")
app.geometry("500x475")

def showSenha():
    print("Senha: " + senha.get())

senha = StringVar()

p_senha = Entry(app, textvariable=senha, show="*")
p_senha.pack()

btn_mostrarSenha = Button(app, text="Mostrar a senha", command=showSenha)
btn_mostrarSenha.pack()

app.mainloop()