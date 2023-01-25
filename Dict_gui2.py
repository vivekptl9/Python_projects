# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 15:40:18 2023

@author: vivek
"""

from difflib import get_close_matches
import json
from tkinter import *
root = Tk()
root.title("Simple Dictionary")
dict_frame = Frame(root)
entry = Entry(root, width=50, borderwidth=5)
entry.pack( padx=10, pady=10)

#word_output = Entry(root, width=60)
#word_output.grid(row=2, column=0, columnspan=3, padx=10, pady=10)
#* ------------------------------------------FUCNCTION TO ACCESS DICTIONARY-----------------------------------------------------------------------
data = json.load(open("data.json"))
def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:  # in case user enters words like USA or NATO
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean %s instead ? \nPlease Enter Yes or No to confirm:  " %get_close_matches(w, data.keys())[0])
        yn = yn.lower()
        if yn == "yes":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "no":
            return "The word does not exist, please check again."
        else:
            return "We did not understand your query."
    else:
        return "The word does not exist, please check again."

#* ------------------------ADDING SCROLLBAR --------------------------------------------------------------------------------------
text_area = Text(root, width=25,height=15,wrap=WORD)
text_area.pack(side=TOP, fill=X)

#* -----------------------ADDING BUTTONS ---------------------------------------------------------------------------------------------
def button_click():
    output = translate(entry.get())
    count = 0
    if type(output) == list:
        for item in output:
            #my_label = Label(root, text=lambda: output[count])
            #my_label.grid(row =iter,column =0,rowspan=10)
            count += 1
            text_area.insert(END, f"{count}. {item}\n")
    else:
        # my_label = Label(root, text= output)
        # my_label.grid(row=2, column=1, rowspan=5)
        text_area.insert(END, output)
    

button_1 = Button(root, text="Defination", padx=40, pady=20,command= button_click)
button_1.pack(padx=1, pady= 1)
root.mainloop()
