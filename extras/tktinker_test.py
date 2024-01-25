# 1.
import tkinter as tk

#2.
window = tk.Tk()
window.title("My first GUI")
window.geometry("300x300")
label_name = tk.Label(text="Teste")
label_name.grid(column=0,row=0)
button_name = tk.Button(window,text="Botão")
button_name.grid(column=1,row=0)
window.mainloop()           # Main loop trava a execução do resto do código

#3.
