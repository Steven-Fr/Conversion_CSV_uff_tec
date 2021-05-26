#! /usr/bin/env python
# -*- coding: UTF-8 -*-

import sys
import os
from tkinter import *
import tkinter
from tkinter import messagebox
import tkinter as tk
import re
from os.path import exists
#test github

testo = ""
top = tkinter.Tk()
top.title("Modify csv file  (© F.Steven)")
top.geometry('320x140') # TODO: test 2

def Check():
    count = 0
    filename = E1.get()
    filename2 = E2.get()
    if(exists(filename)):        #controllo se esiste il file da convertire

        if len(filename2) != 0:     #controllo che sia stato inserito un nome per il file da generare
            lines = []
            with open(filename, 'r') as input:
                lines = input.readlines()
                #print lines
                del lines[0]                                    #elimino prima riga
                del lines[-1]                                   #elimino ultima riga
            conversion = ':'
            newtext = ';'
            outputLines = []
            for line in lines:
                temp = line[:]
                for c in conversion:
                    temp = temp.replace(c, newtext)             #sostituisco ":"" con ";""

                    primo = temp.find(";")                      #trova la posizione del primo ";""
                    temp = temp.replace(temp[0:primo], '')      #elimino quello che c'è prima del PRIMO ";""
                    #temp = re.sub(';.*?;', '?', temp)          #elimina quello che c'è tra 2 ;del;

                    pos = [] #list to store positions for each 'char' in 'string'
                    char = ";"
                    for n in range(len(temp)):
                        if temp[n] == char:
                            pos.append(n)
                    #print pos

                    temp = temp.replace(temp[pos[4]+1:-1], '')   #elimino l'ultima parte prima di andare a capo
                    temp = temp.replace(temp[pos[3]+1:pos[4]], '')   #elimino le varie stringhe dentro i ; tranne la prima che è l'informazione desiderata
                    temp = temp.replace(temp[pos[2]+1:pos[3]], '')
                    temp = temp.replace(temp[pos[1]+1:pos[2]], '')


                    #temp = pulisci(temp, ';',';')
                outputLines.append(temp)

                for char in line:
                    if char in ";":
                        count = count + 1

            with open(filename2, 'w') as output:
                output.write("prima riga sostituita\n")    #aggiungo prima riga di default
                for line in outputLines:                   #ricopio tutte le righe
                    output.write(line)

            L3 = Label(top, text="Edited        \nsuccessfully  ", fg="red")
            L3.pack(padx=50, pady=5)
            L3.place(x=190, y=90)
        else:
            L3 = Label(top, text="Insert name   \noutput file   ", fg="red")
            L3.pack(padx=50, pady=5)
            L3.place(x=190, y=90)

    else:
        L3 = Label(top, text=    "File does     \nnot exist     ", fg="red")
        L3.pack( padx = 50, pady = 5)
        L3.place ( x = 190, y = 90)
        #print "no file input"


#label
L1 = Label(top, text="Insert input file name:")
L1.pack( padx = 50, pady = 5)
L1.place ( x = 10, y = 5)
#entry
E1 = Entry(top, bd =2)
E1.pack(padx = 50, pady = 5)
E1.place(x = 10, y = 35)

#bottone
b = tkinter.Button(top, text= "   Edit   \n   file   ",bd =4 , command = Check )
b.pack(padx = 50, pady = 20)
b.place(x = 190, y = 30)

#label2

L2 = Label(top, text="Insert output file name:")
L2.pack( padx = 50, pady = 5)
L2.place ( x = 10, y = 70)

#entry
E2 = Entry(top, bd =2)
E2.pack(padx = 50, pady = 5)
E2.place(x = 10, y = 100)




def quit():
    top.destroy()
    sys.exit()

#quit
top.protocol('WM_DELETE_WINDOW', quit)


#loop
top.mainloop()