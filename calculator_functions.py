from tkinter import *

def numbers_command(writing_label,x):
    if "." in writing_label.cget("text"):
        
    else:
        number = int(writing_label.cget("text"))
        if number < 0:
            number = (int(writing_label.cget("text")) * 10 ) - x
        else:
            number = (int(writing_label.cget("text")) * 10 ) + x
    writing_label.config(text = str(number))
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