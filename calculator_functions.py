from tkinter import *

def numbers_command(writing_label,x):
     number = 0
     number = (int(writing_label.cget("text")) * 10 ) + x
     writing_label.config(text = str(number))