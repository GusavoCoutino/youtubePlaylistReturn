from tkinter import *
import tkinter
from yt import *
from ytMostViewed import *

root = tkinter.Tk()
root.geometry("450x600")


def get_link(link):
    url = link
    index_first = -1
    index_final = -1
    index_first = url.find("list=") + 5
    index_final = url.find("&index=")
    if index_final != -1:
        list_id = url[index_first:index_final]
    else:
        list_id = url[index_first:]
    if index_first == 4 and index_final == -1:
        return -1
    return list_id


def total_time():
    link = txtUrl.get()
    link = get_link(link)
    if link != -1:
        time = playlist_time(link)
        message = "It would take you " + playlist_time(link) + " to watch this playlist"
        emptylabel.config(text=message, font=("Verdana", 15))
    else:
        emptylabel.config(text="This is not a valid link or is not a video in a playlist", font=("Verdana", 14))


def delete():
    texto.set("")
    emptylabel.config(text="")
    emptylabel2.config(text="")
    emptylabel3.config(text="")
    emptylabel4.config(text="")
    emptylabel5.config(text="")
    emptylabel6.config(text="")
    emptylabel7.config(text="")


def most_viewed():
    link = txtUrl.get()
    link = get_link(link)
    if link != -1:
        videos = views(link)
        emptylabel2.config(text=videos[0], font=("Verdana", 15))
        emptylabel3.config(text=videos[1], font=("Verdana", 15))
        emptylabel4.config(text=videos[2], font=("Verdana", 15))
        emptylabel5.config(text=videos[3], font=("Verdana", 15))
        emptylabel6.config(text=videos[4], font=("Verdana", 15))
    else:
        emptylabel2.config(text="")
        emptylabel3.config(text="")
        emptylabel4.config(text="")
        emptylabel5.config(text="")
        emptylabel6.config(text="")
        emptylabel7.config(text="This is not a valid link or is not a video in a playlist", font=("Verdana", 14))



texto = StringVar()
txtUrl = Entry(root, font="Verdana 22", textvariable=texto)
txtUrl.place(x=60, y=50)
buttonTime = tkinter.Button(root, text='Press', command=total_time)
buttonTime.place(x=280, y=100)
delete = Button(root, text='Delete', command=delete)
delete.place(x=190, y=100)
emptylabel = Label(root)
emptylabel.place(x=30, y=175)
viewed = Button(root, text="Most Viewed", command=most_viewed)
viewed.place(x=60, y=100)
emptylabel2 = Label(root)
emptylabel2.place(x=45, y=220)
emptylabel3 = Label(root)
emptylabel3.place(x=45, y=270)
emptylabel4 = Label(root)
emptylabel4.place(x=45, y=320)
emptylabel5 = Label(root)
emptylabel5.place(x=45, y=370)
emptylabel6 = Label(root)
emptylabel6.place(x=45, y=420)
emptylabel7 = Label(root)
emptylabel7.place(x=30, y=220)
root.mainloop()