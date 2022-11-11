from tkinter import *

def numbers_command(writing_label,x):
    writing_label.config(text = writing_label.cget("text") + str(x))
    
def sign_command(writing_label):
    if "." in writing_label.cget("text"):
        signed_num = float(writing_label.cget("text"))
        signed_num = -1 * (float(writing_label.cget("text")))
        writing_label.config(text = str(signed_num))
    else:
        signed_num = int(writing_label.cget("text"))
        signed_num = -1 * (int(writing_label.cget("text")))
        writing_label.config(text = str(signed_num))
        
def dot_command(writing_label):
    if not("." in writing_label.cget("text")):
        writing_label.config(text = writing_label.cget("text") + ".")

def process_command(writing_label,calculated_label,x):
    if x == "+":
        up_num = float(writing_label.cget("text"))
        down_num = float(calculated_label.cget("text"))
        result = up_num + down_num
        calculated_label.config(text = str(result))
    elif x == "-":
        up_num = float(writing_label.cget("text"))
        down_num = float(calculated_label.cget("text"))
        result = down_num - up_num
        calculated_label.config(text = str(result))
    elif x == "/":
        up_num = float(writing_label.cget("text"))
        down_num = float(calculated_label.cget("text"))
        result = down_num / up_num
        calculated_label.config(text = str(result))
    elif x == "x":
        up_num = float(writing_label.cget("text"))
        down_num = float(calculated_label.cget("text"))
        result = up_num * down_num
        calculated_label.config(text = str(result))
    writing_label.config(text = "")
def clear_command(writing_label,calculated_label):
    writing_label.config(text = "")
    calculated_label.config(text = "0")

def square_percent_command(writing_label,x):
    if x == "x^2":
        squared_num = float(writing_label.cget("text")) ** 2
        writing_label.config(text = squared_num)
    else:
        percent_num = float(writing_label.cget("text")) / 100
        writing_label.config(text = percent_num)