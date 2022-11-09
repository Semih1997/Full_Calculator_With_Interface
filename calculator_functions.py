from tkinter import *

def numbers_command(writing_label,x):
    number = int(writing_label.cget("text"))
    if number < 0:
        number = (int(writing_label.cget("text")) * 10 ) - x
    else:
        number = (int(writing_label.cget("text")) * 10 ) + x
    writing_label.config(text = str(number))
def sign_command(writing_label):
    signed_num = int(writing_label.cget("text"))
    signed_num = -1 * (int(writing_label.cget("text")))
    writing_label.config(text = str(signed_num))