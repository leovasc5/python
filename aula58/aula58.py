from tkinter import *

cfg = ["#041E42", "#fff"]
texto = "Meu primeiro App"

app = Tk()
app.title("App")
app.geometry("500x300")
app.configure(background="#041E42")
txt = Label(app, text=texto, bg=cfg[0], fg=cfg[1])
#txt.place(x=10, y=10, width=150, height=30)
txt.pack(ipadx=20, ipady=20, padx=5, pady=5, side="top", fill=X, expand=True)
app.mainloop()