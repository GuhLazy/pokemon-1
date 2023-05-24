from tkinter import *
import random 
root = Tk()
from PIL import Image, ImageTk

root.title("Pokemon game")
root.geometry("500x500")
root.configure(background="pink")

img = ImageTk.PhotoImage(Image.open("abra.jpg"))
img = ImageTk.PhotoImage(Image.open("bulbasour.jpg"))
img = ImageTk.PhotoImage(Image.open("button.jpg"))
img = ImageTk.PhotoImage(Image.open("charmener.jpg"))
img = ImageTk.PhotoImage(Image.open("Ivyasour.jpg"))
img = ImageTk.PhotoImage(Image.open("jigglypuff.jpg"))
img = ImageTk.PhotoImage(Image.open("kadabra.jpg"))
img = ImageTk.PhotoImage(Image.open("meowth.jpg"))
img = ImageTk.PhotoImage(Image.open("nidoking.jpg"))
img = ImageTk.PhotoImage(Image.open("paras.jpg"))
img = ImageTk.PhotoImage(Image.open("persion.jpg"))
img = ImageTk.PhotoImage(Image.open("pikachu.jpg"))
img = ImageTk.PhotoImage(Image.open("ratata.jpg"))
img = ImageTk.PhotoImage(Image.open("squirtle.jpg"))






root.mainloop()