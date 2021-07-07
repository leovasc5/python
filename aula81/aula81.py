from tkinter import *
from tkinter import ttk

app = Tk()
app.title("Aula 81")
app.geometry("600x300")

listaNomes = [
    ["0", "Alan", "1234"],
    ["1", "Bruno", "4321"],
    ["2", "Charles", "1324"],
    ["3", "Dênis", "4312"]
]

tv = ttk.Treeview(app, columns=("Id", "Nome", "Fone"), show="headings")
tv.column("Id", minwidth=0, width=100)
tv.column("Nome", minwidth=0, width=100)
tv.column("Fone", minwidth=0, width=100)
tv.heading("Id", text="ID")
tv.heading("Nome", text="NOME")
tv.heading("Fone", text="FONE")
tv.pack()


for (a, b, c) in listaNomes:
    tv.insert("", "end",values=(a, b, c))

app.mainloop()