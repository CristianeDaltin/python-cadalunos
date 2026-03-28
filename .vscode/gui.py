import tkinter as tk

#criar a janela principal
janela = tk.Tk()
janela.title("Minha Janela")

#adicionar um label(testo)
label = tk.Label(
    janela,
    text= "Ola, Cris"
)
label.pack()

#inicia o loop da janela
janela.mainloop()


