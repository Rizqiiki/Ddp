from tkinter import *
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

master = Tk()
 #master.config(background="light blue")
 
 #judul aplikasi
judul = Label(text="Kalkulator", font="Normal 20")
judul.grid(row=0, column=0)

 #Konten Aplikasi
nama1 = Label(master, text="Masukan Angka: ", font="Normal 10")
nama1.grid(row=1, column=0)

input1 = Entry(master, font="Normal 10", bd=3)
input1.grid(row=1, column=1)

nama2 = Label(master, text="Masukan Angka: ", font="Normal 10")
nama2.grid(row=2, column=0)

input2 = Entry(master, font="Normal 10", bd=3)
input2.grid(row=2, column=1)

name3 = Label(master, text="Hasil")
name3.grid(row=3, column=0)

Hasil = Label(master, text="0")
Hasil.grid(row=3, column=1)

def tambah():
    Hasil.configure(text=(int(input1.get())+int(input2.get())))

#def perintah():
#   print(input1.get())
#    input1.delete(0, END)

btn = Button(master, text="tambah", command=tambah)
btn.grid(row=3, column=2)

master.mainloop()