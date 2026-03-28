import tkinter as tk

# Cria a janela principal

janela = tk.Tk()

janela.title("Minha Janela")

# Adiciona um label (texto)

label = tk.Label(

janela,

text="Olá, SENAI!"

)

label.pack()

# Inicia o loop da janela

janela.mainloop()