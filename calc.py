from tkinter import *
expression = ""

def press(num):
	global expression
	expression = expression + str(num)
	equation.set(expression)

def equalpress():
	try:
		global expression
		total = str(eval(expression))
		equation.set(total)
		expression = ""
	except:

		equation.set(" error ")
		expression = ""

def clear():
	global expression
	expression = ""
	equation.set("")


if __name__ == "__main__":
    gui = Tk()
 
    # set the background colour of GUI window
    gui.configure(background="white")
 
    # set the title of GUI window
    gui.title("Simple Calculator")
 
    # set the configuration of GUI window
    gui.geometry("300x180")
 
    # StringVar() is the variable class
    # we create an instance of this class
    equation = StringVar()
	
    expression_field = Entry(gui, textvariable=equation)
	
    expression_field.grid(columnspan=5, ipadx=70)
	
    button1 = Button(gui, text=' 1 ', fg='black', bg='light blue',command=lambda: press(1), height=1, width=4)
	
    button1.grid(row=5, column=0)

	
    button2 = Button(gui, text=' 2 ', fg='black', bg='light blue',command=lambda: press(2), height=1, width=4)
	
    button2.grid(row=5, column=1)

	
    button3 = Button(gui, text=' 3 ', fg='black', bg='light blue',command=lambda: press(3), height=1, width=4)
	
    button3.grid(row=5, column=2)

	
    button4 = Button(gui, text=' 4 ', fg='black', bg='light blue',command=lambda: press(4), height=1, width=4)
	
    button4.grid(row=4, column=0)

	
    button5 = Button(gui, text=' 5 ', fg='black', bg='light blue',command=lambda: press(5), height=1, width=4)
	
    button5.grid(row=4, column=1)

	
    button6 = Button(gui, text=' 6 ', fg='black', bg='light blue',command=lambda: press(6), height=1, width=4)
	
    button6.grid(row=4, column=2)

	
    button7 = Button(gui, text=' 7 ', fg='black', bg='light blue',command=lambda: press(7), height=1, width=4)
	
    button7.grid(row=3, column=0)

	
    button8 = Button(gui, text=' 8 ', fg='black', bg='light blue',command=lambda: press(8), height=1, width=4)
	
    button8.grid(row=3, column=1)

	
    button9 = Button(gui, text=' 9 ', fg='black', bg='light blue',command=lambda: press(9), height=1, width=4)
	
    button9.grid(row=3, column=2)

	
    button0 = Button(gui, text=' 0 ', fg='black', bg='light blue',command=lambda: press(0), height=1, width=4)
	
    button0.grid(row=6, column=0)

	
    plus = Button(gui, text=' + ', fg='black', bg='light green',command=lambda: press("+"), height=1, width=4)
	
    plus.grid(row=4, column=3)

	
    minus = Button(gui, text=' - ', fg='black', bg='light green',command=lambda: press("-"), height=1, width=4)
	
    minus.grid(row=5, column=3)

	
    multiply = Button(gui, text=' * ', fg='black', bg='light green',command=lambda: press("*"), height=1, width=4)
	
    multiply.grid(row=2, column=3)

	
    divide = Button(gui, text=' / ', fg='black', bg='light green',command=lambda: press("/"), height=1, width=4)
	
    divide.grid(row=3, column=3)

	
    equal = Button(gui, text=' = ', fg='black', bg='red',command=equalpress, height=1, width=4)
	
    equal.grid(row=6, column=3)

	
    clear = Button(gui, text='Clear', fg='black', bg='cyan',command=clear, height=1, width=4)
	
    clear.grid(row=2, column=0)

	
    Decimal= Button(gui, text='.', fg='black', bg='light blue',command=lambda: press('.'), height=1, width=4)
	
    Decimal.grid(row=6, column=1)

    gui.mainloop()
