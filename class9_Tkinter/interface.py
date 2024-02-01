from tkinter import *
from tkinter import messagebox

def showmessage():
    messagebox("Boas vindas","Olá " + caixa_nome.get())
    pass
window = Tk()
window.geometry("400x400")

label_nome = Label(window,text="Insira seu nome: ")
caixa_nome = Entry(cursor="heart")
btn_nome = Button(window,text="confirmar",command=showmessage,background="green")


label_nome.pack(side="left",)
caixa_nome.pack(side="left")
btn_nome.pack(side="left")
window.mainloop()