from tkinter import *
from tkinter import ttk
import random as rd
from PIL import ImageTk, Image


class janela_principal():
    def __init__(self, *args, **kwargs):
        self.janela = Tk()
        self.abrir_janela()
        
        
    def gerar_senha(self, *args, **kwargs):
        digitos = ['a', 'b', 'c', 'd', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
                   'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '#', '$', '%']
        
        try:
            numr_lista = int(self.entry_caracteres.get())
        except ValueError:
            return
        
        n_lista = []
        
        for i in range(numr_lista):
            n_lista.append(digitos[rd.randint(0, len(digitos)-1)])
        
        password = ''.join(n_lista)
        
        self.senha_gerada.config(text=f"senha={password}")
        
    def abrir_janela(self, *args, **kwargs):
        self.janela.geometry('500x500')
        self.janela.title('Gerador de senhas')
        
        cor1 = '#ccd6e0' 

        self.frame_principal = Frame(self.janela, width=500, height=500, bg=cor1)
        self.frame_principal.place(x=0, y=0)
        
        self.label_Titulo = Label(self.frame_principal, text='GERADOR DE SENHAS',bg= cor1, font='Temple 18 bold')
        self.label_Titulo.place(x=10, y=10)
        
        self.label_caracteres = Label(self.frame_principal, text='caracteres:', font='Arial 12 bold', bg=cor1, fg='black')
        self.label_caracteres.place(x=10, y=100)
        
        
        self.entry_caracteres = Entry(self.frame_principal, width=10, font='Arial 12 bold', relief='solid')
        self.entry_caracteres.place(x=100, y=100)
        
        self.btn_gerar = Button(self.frame_principal, text= 'gerar', command=self.gerar_senha,
                         font='Arial 12 bold', bg='blue', fg='white', relief='solid', width=8, height=2 )
        self.btn_gerar.place(x=20, y=150)
        
        self.senha_gerada = Label(self.frame_principal, text='senha=',font='Arial 12 bold', bg=cor1, fg='red')
        self.senha_gerada.place(x=10, y=400)
        
        self.janela.mainloop()
        
        
app = janela_principal()
