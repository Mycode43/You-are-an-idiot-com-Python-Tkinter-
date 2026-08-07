#------------ Importing tkinter library--------
import tkinter as tk
from tkinter import *
from tkinter import messagebox
# ---------Importing pygame library-----------
import pygame
from pygame import *


#----------Random notes---------------
"""
janela1 = tk.Tk()
janela1.geometry("700x700")
janela1.title = "You are an idiot"

#janela1.resizable(False, False)

janela1.configure(bg="white")

imagem = tk.PhotoImage(file="you_are_an_idiot_2.png")
label1 = tk.Label(janela1, image=imagem)

label1.pack()

janela1.mainloop()
"""

# -----lists------
janelas = []
fotos = []


#-----initial window and your configs-----
janela_inicial = tk.Tk()
janela_inicial.resizable(False, False)
janela_inicial.geometry('600x800')

pygame.init()
pygame.mixer.music.load("musica_do_meme.mp3")
pygame.mixer.music.play(-1)
#----------------Image------------------------------
image1 = tk.PhotoImage(file="you_are_an_idiot_2.png")
image1 = image1.zoom(1)
label = tk.Label(janela_inicial, image=image1)

#_____

def avisar_fechamento():
    messagebox.showinfo('Aviso, você não pode fechar essa janela. You are an idiot hahahahaha')



janela_inicial.protocol("WM_DELETE_WINDOW", avisar_fechamento)

def duplication(janela_para_fechar):
        janela_para_fechar.destroy()


        for i in range(2):
            nova = tk.Toplevel(janela_inicial)
            nova.title("You are an idiot")
            nova.geometry("800x800")

            fota = tk.PhotoImage(file="you_are_an_idiot_2.png")
            lbl = tk.Label(nova, image=fota)
            lbl.place(x=50, y=150)

            # Faz as novas janelas duplicarem tbm
            nova.protocol("WM_DELETE_WINDOW", lambda j=nova: duplication(j))
            fotos.append(fota)
            janelas.append(nova)





#-----Defs dos botoes da janela_inicial------
def botao_yes():
    print("Botao 1")



    for i in range(0,30):

        
        #-------Janelas----------------
        janela = tk.Toplevel(janela_inicial)
        janela.resizable(False, False)
        janela.geometry("800x800")

        janela.protocol("WM_DELETE_WINDOW", lambda j=janela: duplication(j))
        #-------fotos e seus labels------
        foto = tk.PhotoImage(file="you_are_an_idiot_2.png")
        foto = foto.zoom(2)
        labels = tk.Label(janela, image=foto)
        labels.place(x=50, y=150)

        janelas.append(janela)
        fotos.append(foto)




def botao_no():
    print("Button 2(no)")

   


    for i in range(0,30):

        #-------Janelas----------------
        janela = tk.Toplevel(janela_inicial)
        janela.resizable(False, False)
        janela.geometry('800x800')

        janela.protocol("WM_DELETE_WINDOW", lambda j=janela: duplication(j))
        #-------fotos e seus labels------
        foto = tk.PhotoImage(file="you_are_an_idiot_2.png")
        foto = foto.zoom(2)
        labels = tk.Label(janela, image=foto)
        labels.place(x=50, y=10)

        janelas.append(janela)
        fotos.append(foto)



#-----------Buttons for window 1---------------------
button1 = tk.Button(janela_inicial)
button1.configure(text='Yes',
                  font=('Arial', 30),
                  fg="green",
                  command=botao_yes)
button2 = tk.Button(janela_inicial)
button2.configure(text='No',
                  font=('Arial', 30),
                  fg="red",
                  command=botao_no)




button1.place(x=60, y=590)
button2.place(x=210, y=590)

label.place(x=50, y=150)

janela_inicial.mainloop()

