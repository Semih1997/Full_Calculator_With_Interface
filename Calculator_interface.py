from tkinter import *
from tkinter.ttk import *  #import this because to determine buttons style easier.

buttons_height = 50
buttons_width = 70
numbers_color = "red"
signs_color = "blue"
equal_color = "orange"

calculator_screen = Tk()            #screen opening.

calculator_screen.title("CALCULATOR")
calculator_screen.geometry("490x400")

style = Style()  # **tkinter.ttk**
 
style.configure('TButton', font =
               ('calibri', 15, 'bold'),
                    borderwidth = '4')    #TButton apply this style all buttons.
style.map('TButton', foreground = [('active', '!disabled', 'green')]) 

sign_button = Button(calculator_screen,text="+/-",command= None)
sign_button.place(x=0,y=350,height=buttons_height,width=buttons_width)
button_0 = Button(calculator_screen,text="0",command=None)
button_0.place(x=70,y=350,height=buttons_height,width=buttons_width)
button_dot = Button(calculator_screen,text=".",command=None)
button_dot.place(x=140,y=350,height=buttons_height,width=buttons_width)
button_equal = Button(calculator_screen,text="=",command=None)
button_equal.place(x=210,y=350,height=buttons_height,width=buttons_width)
button_1 = Button(calculator_screen,text="1",command=None)
button_1.place(x=0,y=300,height=buttons_height,width=buttons_width)
button_2 = Button(calculator_screen,text="2",command=None)
button_2.place(x=70,y=300,height=buttons_height,width=buttons_width)
button_3 = Button(calculator_screen,text="3",command=None)
button_3.place(x=140,y=300,height=buttons_height,width=buttons_width)
button_plus = Button(calculator_screen,text="+",command=None)
button_plus.place(x=210,y=300,height=buttons_height,width=buttons_width)
button_4 = Button(calculator_screen,text="4",command=None)
button_4.place(x=0,y=250,height=buttons_height,width=buttons_width)
button_5 = Button(calculator_screen,text="5",command=None)
button_5.place(x=70,y=250,height=buttons_height,width=buttons_width)
button_6 = Button(calculator_screen,text="6",command=None)
button_6.place(x=140,y=250,height=buttons_height,width=buttons_width)
button_minus = Button(calculator_screen,text="-",command=None)
button_minus.place(x=210,y=250,height=buttons_height,width=buttons_width)
button_7 = Button(calculator_screen,text="7",command=None)
button_7.place(x=0,y=200,height=buttons_height,width=buttons_width)
button_8 = Button(calculator_screen,text="8",command=None)
button_8.place(x=70,y=200,height=buttons_height,width=buttons_width)
button_9 = Button(calculator_screen,text="9",command=None)
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