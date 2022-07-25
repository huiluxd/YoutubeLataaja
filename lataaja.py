#Youtube Lataaja
#Meikän tekemä!
import os
from tkinter.ttk import Widget
from pytube import YouTube
import tkinter as tk
import pathlib

desktop = pathlib.Path.home()
# link = argv[1]

#Punainen ulkokuori
rt = tk.Tk()
canvas = tk.Canvas(rt, height=150, width=500, bg="#b00b1e")
canvas.pack()

#Valkoinen sisäkuori
frame = tk.Frame(rt, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

#Yläteksti
otsikko = tk.Label(rt, text='Laita ensin linkki, jonka jälkeen paina latausnappia.')
otsikko.config(font=('Comic Sans MS',12),borderwidth=2)
otsikko.place(relwidth=0.8, relheight=1, relx=0.1, rely=-0.3)

inputbox1 = tk.Entry(rt,width = 70, borderwidth=5)
inputbox1.place(width=404,height=25, relx=0.1, rely=0.3)
# canvas.create_window(300, 140, window=inputbox1)
def siivoa(x):
    Widget.destroy(x)
def lataa_aani():
    i = inputbox1.get()
    yt = YouTube(i)
    try:
        aanitiedosto = yt.streams.get_by_itag(22).download()
        base, ext = os.path.splitext(aanitiedosto)
        uusitiedosto = base + '.mp3'
        os.rename(aanitiedosto, uusitiedosto)
        valmis = tk.Label(rt, text='Äänitiedosto ladattu onnistuneesti.')
        valmis.place(relwidth=0.8, relheight=1, relx=0.1, rely=-0.3)
        valmis.config(font=('Comic Sans MS',10),borderwidth=3)
        rt.after(1200, siivoa, valmis)
    except FileExistsError:
        loytyyjo = tk.Label(rt, text='Tiedosto löytyy jo kansiosta!')
        loytyyjo.place(relwidth=0.8, relheight=1, relx=0.1, rely=-0.3)
        loytyyjo.config(font=('Comic Sans MS',10),borderwidth=3)
        rt.after(1200, siivoa, loytyyjo)
    else:
        rt.after(1200, siivoa, valmis)

laaninappi = tk.Button(rt, text="Lataa äänitiedosto", font=('Comic Sans MS',8),padx=10, pady=10, bg="#b00b1e", command=lataa_aani)
laaninappi.place(relx=0.375, rely=0.55)
rt.mainloop()

