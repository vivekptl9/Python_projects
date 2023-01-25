# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 15:40:18 2023

@author: vivek
"""

from tkinter import *
root = Tk()
root.title("Simple Calculator")

entry = Entry(root, width = 35, borderwidth = 5)
entry.grid(row=0,column=0,columnspan =3, padx=10, pady =10)

#* ------------------------------------------BUTTONS----------------------------------------------------------------------------------------------------- 
def button_click(number):
    current=entry.get()
    entry.delete(0,END)
    entry.insert(0,str(current)+str(number))
 
#TODO ----------------------------------------IMPLEMENT IT LATER-----------------------------------------------------------------------------------------
'''def button_brac1():
    current=entry.get()
    entry.insert(0,"(")
    
def button_brac2():
    current=entry.get()
    entry.insert(0,")")'''
#TODO --------------------------------------------------------------------------------------------------------------------------------------------------    
def button_clear():
     entry.delete(0,END)
     
def button_sum():
    first_num = entry.get()
    global f_num
    global math 
    math = "add"
    f_num = int(first_num)
    entry.delete(0,END)

def button_sub():
    first_num = entry.get()
    global f_num
    global math 
    math = "sub"
    f_num = int(first_num)
    entry.delete(0,END)
        
def button_mul():
    first_num = entry.get()
    global f_num
    global math 
    math = "mul"
    f_num=int(first_num)
    entry.delete(0,END)

def button_pow():
    first_num = entry.get()
    global f_num
    global math 
    math = "pow"
    f_num=int(first_num)
    entry.delete(0,END)
     
def button_div():
    first_num = entry.get()
    global f_num
    global math 
    math = "div"
    f_num=int(first_num)
    entry.delete(0,END)
    
def button_equal():
     second_num = entry.get()
     entry.delete(0,END)
     if math == "add":
         entry.insert(0, f_num + int(second_num))
     if math == "sub":
         entry.insert(0, f_num - int(second_num))
     if math == "mul":
         entry.insert(0, f_num * int(second_num))
     if math == "div":
         entry.insert(0, f_num / int(second_num))
     if math == "pow":
         entry.insert(0, f_num ** int(second_num))


#* ---------------------------------------BUTTONS--------------------------------------------------------------------------------------------------------

button_1 =  Button(root, text = "1", padx = 40, pady = 20, command = lambda: button_click(1))
button_2 =  Button(root, text = "2", padx = 40, pady = 20, command = lambda: button_click(2))
button_3 =  Button(root, text = "3", padx = 40, pady = 20, command = lambda: button_click(3))
button_4 =  Button(root, text = "4", padx = 40, pady = 20, command = lambda: button_click(4))
button_5 =  Button(root, text = "5", padx = 40, pady = 20, command = lambda: button_click(5))
button_6 =  Button(root, text = "6", padx = 40, pady = 20, command = lambda: button_click(6))
button_7 =  Button(root, text = "7", padx = 40, pady = 20, command = lambda: button_click(7))
button_8 =  Button(root, text = "8", padx = 40, pady = 20, command = lambda: button_click(8))
button_9 =  Button(root, text = "9", padx = 40, pady = 20, command = lambda: button_click(9))
button_0 =  Button(root, text = "0", padx = 40, pady = 20, command = lambda: button_click(0))
button_sum =  Button(root, text = "+", padx = 38, pady = 20, command = button_sum)
button_equal =  Button(root, text = "=", padx = 88, pady = 20, command = button_equal)
button_clear =  Button(root, text = "Clear", padx = 79, pady = 20, command = button_clear)

button_sub =  Button(root, text = "-", padx = 40, pady = 20, command = button_sub)
button_mul =  Button(root, text = "*", padx = 40, pady = 20, command = button_mul)
button_div =  Button(root, text = "/", padx = 40, pady = 20, command = button_div)
button_pow =  Button(root, text = "x^y", padx = 31, pady = 20, command = button_pow)

#button_brac1 =  Button(root, text = "(", padx = 40, pady = 20, command = button_brac1)
#button_brac2 =  Button(root, text = ")", padx = 40, pady = 20, command = button_brac2)


button_1.grid(row = 3,column = 0)
button_2.grid(row = 3,column = 1)
button_3.grid(row = 3,column = 2)

button_4.grid(row = 2,column = 0)
button_5.grid(row = 2,column = 1)
button_6.grid(row = 2,column = 2)

button_7.grid(row = 1,column = 0)
button_8.grid(row = 1,column = 1)
button_9.grid(row = 1,column = 2)

button_0.grid(row = 4,column = 0 )
button_clear.grid(row = 5,column=0, columnspan = 2)
button_sum.grid(row = 4,column= 3)
button_equal.grid(row = 4,column=1, columnspan = 2)

button_sub.grid(row = 3,column= 3)
button_mul.grid(row = 2,column= 3)
button_div.grid(row = 1,column= 3)
button_pow.grid(row = 5,column= 3)
#button_brac1.grid(row = 5,column= 0)
#button_brac2.grid(row = 5,column= 3)

root.mainloop()