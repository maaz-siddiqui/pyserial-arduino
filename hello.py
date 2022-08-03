from curses import baudrate
from glob import glob
from multiprocessing.connection import wait
from pickle import TRUE
from sys import displayhook
from textwrap import fill
import serial
import tkinter
import customtkinter
from tkinter import StringVar, ttk
from tkinter.messagebox import showinfo
import time

toggle = 0
port = 'none'
comPort = 'com7'
ser = 0
intr = 0

def blink():
    i=0
    while(i<10):
        led()
        time.sleep(1/4)
        led()
        time.sleep(1/4)
        i+=1


def portCall():
    global port
    port = comPort.get()
    global ser
    ser = serial.Serial(port, 115200)
    top.update_idletasks()

def led():
    global toggle
    if(toggle):
        toggle = 0
        onCall()
    else: 
        toggle = 1
        offCall()

def onCall():
    global ser
    cmd = "h"
    cmd+='\r'
    ser.write(cmd.encode())

def offCall():
    global ser
    cmd = "l"
    cmd+='\r'
    ser.write(cmd.encode())

#WINDOW RENDER
top = customtkinter.CTk()
top.geometry("300x170")
customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("blue")
top.title("TOGGLE LED")
top.resizable(True, True)
top.iconbitmap(r'C:\Users\Maaz Siddiqui\Desktop\python_gui\tkinter\icon.ico')
comPort = tkinter.StringVar()

comEntry = customtkinter.CTkLabel(top, text="Enter Com Port (i.e com7) : ")
comEntry.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)
comEntry.pack(fill='x', expand=True)

comEntry = customtkinter.CTkEntry(top, textvariable=comPort, width=240)
comEntry.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)
comEntry.pack()
comEntry.focus()

C = customtkinter.CTkButton(top, text ="Select Port", command = portCall, width=240)
C.place(anchor=tkinter.CENTER)
C.pack(pady=5)

B = customtkinter.CTkButton(top, text ="Toggle", command = led, width=240)
B.place(relx=0.5, y=0.5, anchor=tkinter.CENTER)
B.pack(pady=5)

D = customtkinter.CTkButton(top, text="Blinky", command = blink, width=240)
D.place(relx=0.3333, rely=0.5, anchor=tkinter.CENTER)
D.pack(pady=5)

top.mainloop()