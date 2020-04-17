from tkinter import *   # tkinter --Tkinter is the standard GUI library for Python.
from tkinter import messagebox

# to display the numbers and operators
def buttonclick(number):
    global operator
    operator = operator + str(number)   # for 2 or more digit numbers
    text_Input.set(operator)  # set- to store the value into the variable,text_Input

# Clear button
def btnClearDisplay():
    global operator
    operator=""
    text_Input.set(operator)

# Equals button
def EqualsInput():
    global operator
    if "/0" in operator:
        messagebox.showerror("Error", "Zero Divisioion Error")
    sumup = str(eval(operator))   # the eval function evaluates the “String” like a python expression
                                # and returns the result as an integer.

    text_Input.set(sumup)
    operator = ""

cal = Tk()                      # Tkinter works by starting a tcl/tk interpreter,
                                # Creating an instance of Tk initializes this interpreter and creates the root window.
cal.title("Calculator")
operator = ""
text_Input=StringVar()  # Holds a string; default value ""

text_display=Entry(cal,font=('arial',15,'bold'),bd=30,bg="powder blue",textvariable=text_Input,
                   justify="right").grid(columnspan=4)   # 4 columns , #textvariable=text_Input
                # The Entry widget is used to accept single-line text strings from a user.



# The Button widget is used to add buttons in a Python application.
btn7=Button(cal,padx=16,pady=12,bd=8,fg="black",font=('arial',20,'bold'),text="7",command=lambda:buttonclick(7)).grid(row=1,column=0)
btn8 = Button(cal, padx=16,pady=12, bd=8, fg="black", font=('arial', 20, 'bold'), text="8",command=lambda:buttonclick(8)).grid(row=1, column=1)
btn9 = Button(cal, padx=16,pady=12, bd=8, fg="black", font=('arial', 20, 'bold'), text="9",command=lambda:buttonclick(9)).grid(row=1, column=2)
btnAddition = Button(cal, padx=16, pady=12,bd=8, fg="black", font=('arial', 20, 'bold'), text="+",command=lambda:buttonclick("+")).grid(row=1, column=3)

btn4=Button(cal,padx=16,pady=12,bd=8,fg="black",font=('arial',20,'bold'),text="4",command=lambda:buttonclick(4)).grid(row=2,column=0)
btn5 = Button(cal, padx=16,pady=12, bd=8, fg="black", font=('arial', 20, 'bold'), text="5",command=lambda:buttonclick(5)).grid(row=2, column=1)
btn6 = Button(cal, padx=16,pady=12, bd=8, fg="black", font=('arial', 20, 'bold'), text="6",command=lambda:buttonclick(6)).grid(row=2, column=2)
btnSubstraction = Button(cal, padx=16,pady=12, bd=8, fg="black", font=('arial', 20, 'bold'), text="-",command=lambda:buttonclick("-")).grid(row=2, column=3)

btn1=Button(cal,padx=16,pady=12,bd=8,fg="black",font=('arial',20,'bold'),text="1",command=lambda:buttonclick(1)).grid(row=3,column=0)
btn2 = Button(cal, padx=16, pady=12,bd=8, fg="black", font=('arial', 20, 'bold'), text="2",command=lambda:buttonclick(2)).grid(row=3, column=1)
btn3 = Button(cal, padx=16, pady=12,bd=8, fg="black", font=('arial', 20, 'bold'),command=lambda:buttonclick(3), text="3").grid(row=3, column=2)
btnMultiply = Button(cal, padx=16,pady=12, bd=8, fg="black", font=('arial', 20, 'bold'), text="*",command=lambda:buttonclick("*")).grid(row=3, column=3)

btn0=Button(cal,padx=16,pady=12,bd=8,fg="black",font=('arial',20,'bold'),text="0",command=lambda:buttonclick(0)).grid(row=4,column=0)
btnClear = Button(cal, padx=16,pady=12, bd=8, fg="black", font=('arial', 20, 'bold'), text="C",command=btnClearDisplay).grid(row=4, column=1)
btnEquals = Button(cal, padx=16,pady=12, bd=8, fg="black", font=('arial', 20, 'bold'), text="=",command=EqualsInput).grid(row=4, column=2)
btnDivision= Button(cal, padx=16,pady=12, bd=8, fg="black", font=('arial', 20, 'bold'), text="/",command=lambda:buttonclick("/")).grid(row=4, column=3)


cal.mainloop()    # There is a method known by the name mainloop() is used when your application is ready to run.
                # mainloop() is an infinite loop used to run the application, wait for an event to occur
                # and process the event as long as the window is not closed.
