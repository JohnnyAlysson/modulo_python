from tkinter import *
from tkinter import messagebox

def somar():
    soma = int(caixa_num1.get()) + int(caixa_num2.get()) #get pegar o valor do Entry
    messagebox.showinfo("resultado",soma)
def subtrair():
    subtracao = int(caixa_num1.get()) - int(caixa_num2.get()) #get pegar o valor do Entry
    messagebox.showinfo("resultado",subtracao)
def multiplicar():
    multipli = int(caixa_num1.get()) * int(caixa_num2.get()) #get pegar o valor do Entry
    messagebox.showinfo("resultado",multipli)
def dividir():
    divid = int(caixa_num1.get()) / int(caixa_num2.get()) #get pegar o valor do Entry
    messagebox.showinfo("resultado",divid)
    

#inicio configuração de página
window = Tk () #janela recebe a class LK
window.title("Calculadora")
window.iconbitmap("class9_Tkinter\calc.ico")
window.geometry("600x400+600+200")
# window.resizable(False,False)
window.minsize(400,200)

#Widget
num1 = Label(window,text="Informe o primeiro número: ",
            foreground= "blue",
            font=("Arial",20,"bold")
            )
caixa_num1 = Entry(cursor="heart")
num2 = Label(window,text="Informe o segundo número: ",
            foreground= "blue",
            font=("Arial",20,"bold")
            )
caixa_num2 = Entry(insertborderwidth=5)
btn_somar = Button(window,
                    text="Somar",
                    command=somar
                    )
btn_subtrair = Button(window,
                    text="subtrair",
                    command=subtrair
                    )
btn_multiplicar = Button(window,
                    text="multiplicar",
                    command=multiplicar
                    )
btn_dividir = Button(window,
                    text="dividir",
                    command=dividir
                    )




#posicionamento
num1.pack()
caixa_num1.pack()
num2.pack()
caixa_num2.pack()
btn_somar.pack()
btn_subtrair.pack()
btn_multiplicar.pack()
btn_dividir.pack()


window.mainloop() #chamada do método o objeto, nesse caso mainloop para a janela aparecer e ficar em loop