#-----------Bolierplate Code Start -----
#cd C:\Users\AwesomeGamer\Downloads\module5\C-208
import socket
from threading import Thread
from tkinter import *
from tkinter import ttk
from playsound import playsound
import pygame
from pygame import mixer
import os
import time


PORT  = 8080
IP_ADDRESS = '127.0.0.1'
SERVER = None
BUFFER_SIZE = 4096

name = None
listbox = None
textarea = None
labelchat = None
text_message = None

def play():
    global song_selected
    song_selected = listbox.get(ANCHOR)

    pygame
    mixer.init()
    mixer.music.load('shared_files/'+ song_selected)
    mixer.music.play()
    if(song_selected != ""):
        infoLabel.configure(text = "now playing:"+ song_selected)
    else:
        infoLabel.configure(text = "")

def stop():
    global song_selected

    pygame
    mixer.init()
    mixer.music.load('shared_files/'+ song_selected)
    mixer.music.pause()
    infoLabel.configure(text="")




def recieveMessage():
    global SERVER
    global BUFFER_SIZE

    while True:
        chunk = SERVER.recv(BUFFER_SIZE)
        try:
            if("tiul" in chunk.decode() and "1.0" not in chunk.decode()):
                letter_list = chunk.decode().split(",")
                listbox.insert(letter_list[0],letter_list[0]+":"+letter_list[1]+":"+letter_list[3]+" "+letter_list[5])
                print(letter_list[0],letter_list[0]+":"+letter_list[1]+":"+letter_list[3]+" "+letter_list[5])
            else:
                textarea.insert(END,"\n"+chunk.decode("ascii"))
                textarea.see("end")
                print(chunk.decode("ascii"))
        except:
            pass

def showClientList():
    global listbox
    listbox.delete(0,"end")
    SERVER.send("show list".encode("ascii"))    

def connectToServer():
    global SERVER
    global name
    global sending_file
    cname = name.get()
    SERVER.send(cname.encode())

def musicWindow():
    window = Tk()
    window.title("Music Window")
    window.geometry("300x300")
    window.configure(bg="#82bd29")
    global name 
    global listbox 
    global textarea 
    global labelchat 
    global text_message
    global filepathlabel

    nameLabel = Label(window,text="enter song", font=("Calibri",10))
    nameLabel.place(x=2,y=1)
   
    listbox = Listbox(window,height=10, width=39, activestyle='dotbox', bg="#238db3", font=("Calibri",10))
    listbox.place(x=10,y=10)

    scrollbar1 = Scrollbar(listbox)
    scrollbar1.place(relheight=1, relx=1)
    scrollbar1.config(command = listbox.yview)

    PlayButton = Button(window, text="Play", width=10,bd=1,bg="#182bda", font=("Calibri",10), command=play)
    PlayButton.place(x=30,y=200)

    StopButton = Button(window, text="Stop", width=10,bd=1,bg="#182bda", font=("Calibri",10), command=stop)
    StopButton.place(x=200,y=200)

    UploadButton = Button(window, text="Stop", width=10,bd=1,bg="#182bda", font=("Calibri",10))
    UploadButton.place(x=30,y=250)

    infoLabel = Label(window, text="", fg="blue", font=("Calibri",10))
    infoLabel.place(x=4,y=280)



    window.mainloop()
    




def setup():
    global SERVER
    global PORT
    global IP_ADDRESS

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS, PORT))
    
    musicWindow()
setup()


#-----------Bolierplate Code Start -----