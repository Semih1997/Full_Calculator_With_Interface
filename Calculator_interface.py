from tkinter import *
from tkinter.ttk import *  #import this because to determine buttons style easier.
from calculator_functions import numbers_command, sign_command

buttons_height = 50
buttons_width = 70
numbers_color = "red"
signs_color = "blue"
equal_color = "orange"

calculator_screen = Tk()            #screen opening

calculator_screen.title("CALCULATOR")
calculator_screen.geometry("490x400")

style = Style()  # **tkinter.ttk**
 
style.configure('TButton', font =
               ('calibri', 15, 'bold'),
                    borderwidth = '4')    #TButton apply this style all buttons. If we make W.TButton we can apply buttons which we want. 
style.map('TButton', foreground = [('active', '!disabled', 'green')])

#LABELS
writing_label = Label(calculator_screen,text="0",font=("calibri",17,"bold"))
writing_label.place(x=0,y=0,height=50,width=490)
writing_label.configure(background="orange")
calculated_label = Label(calculator_screen,text="")
calculated_label.place(x=0,y=50,height=100,width=490)
calculated_label.configure(background="green")

#BUTTONS
sign_button = Button(calculator_screen,text="+/-",command=lambda: sign_command(writing_label))
sign_button.place(x=0,y=350,height=buttons_height,width=buttons_width)
button_0 = Button(calculator_screen,text="0",command=lambda: numbers_command(writing_label,0))
button_0.place(x=70,y=350,height=buttons_height,width=buttons_width)
button_dot = Button(calculator_screen,text=".",command=None)
button_dot.place(x=140,y=350,height=buttons_height,width=buttons_width)
button_equal = Button(calculator_screen,text="=",command=None)
button_equal.place(x=210,y=350,height=buttons_height,width=buttons_width)
button_1 = Button(calculator_screen,text="1",command=lambda: numbers_command(writing_label,1))
button_1.place(x=0,y=300,height=buttons_height,width=buttons_width)
button_2 = Button(calculator_screen,text="2",command=lambda: numbers_command(writing_label,2))
button_2.place(x=70,y=300,height=buttons_height,width=buttons_width)
button_3 = Button(calculator_screen,text="3",command=lambda: numbers_command(writing_label,3))
button_3.place(x=140,y=300,height=buttons_height,width=buttons_width)
button_plus = Button(calculator_screen,text="+",command=None)
button_plus.place(x=210,y=300,height=buttons_height,width=buttons_width)
button_4 = Button(calculator_screen,text="4",command=lambda: numbers_command(writing_label,4))
button_4.place(x=0,y=250,height=buttons_height,width=buttons_width)
button_5 = Button(calculator_screen,text="5",command=lambda: numbers_command(writing_label,5))
button_5.place(x=70,y=250,height=buttons_height,width=buttons_width)
button_6 = Button(calculator_screen,text="6",command=lambda: numbers_command(writing_label,6))
button_6.place(x=140,y=250,height=buttons_height,width=buttons_width)
button_minus = Button(calculator_screen,text="-",command=None)
button_minus.place(x=210,y=250,height=buttons_height,width=buttons_width)
button_7 = Button(calculator_screen,text="7",command=lambda: numbers_command(writing_label,7))
button_7.place(x=0,y=200,height=buttons_height,width=buttons_width)
button_8 = Button(calculator_screen,text="8",command=lambda: numbers_command(writing_label,8))
button_8.place(x=70,y=200,height=buttons_height,width=buttons_width)
button_9 = Button(calculator_screen,text="9",command=lambda: numbers_command(writing_label,9))
button_9.place(x=140,y=200,height=buttons_height,width=buttons_width)
button_multiple = Button(calculator_screen,text="x",command=None)
button_multiple.place(x=210,y=200,height=buttons_height,width=buttons_width)
button_clear = Button(calculator_screen,text="C",command=None)
button_clear.place(x=0,y=150,height=buttons_height,width=buttons_width)
button_parantesies = Button(calculator_screen,text="( )",command=None)
button_parantesies.place(x=70,y=150,height=buttons_height,width=buttons_width)
button_percent = Button(calculator_screen,text="%",command=None)
button_percent.place(x=140,y=150,height=buttons_height,width=buttons_width)
button_divide = Button(calculator_screen,text="/",command=None)
button_divide.place(x=210,y=150,height=buttons_height,width=buttons_width)

calculator_screen.resizable(False,False)
calculator_screen.mainloop()