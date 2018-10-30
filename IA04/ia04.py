from tkinter import *
from tkinter import messagebox

window=Tk() # TK method that creates a windows objective
window.wm_title("Compute a savings plan")

# Adding labels
l1=Label(window, text="Years")
l1.grid(row=0,column=0)

l2=Label(window, text="Interest Rate")
l2.grid(row=1,column=0)

l3=Label(window, text="Final Balance")
l3.grid(row=2,column=0)

l3=Label(window, text="Initial Balance")
l3.grid(row=0,column=2)

l3=Label(window, text="Monthly Deposit")
l3.grid(row=1,column=2)

# Adding text input fields
year_text=StringVar()
e1=Entry(window,textvariable=year_text, width=20)
e1.grid(row=0,column=1)

interest_rate_text=StringVar()
e2=Entry(window,textvariable=interest_rate_text, width=20)
e2.grid(row=1,column=1)

final_balance_text=StringVar()
e3=Entry(window,textvariable=final_balance_text, width=20)
e3.grid(row=2,column=1)
e3.configure(state=DISABLED)

init_bal_text=StringVar()
e4=Entry(window,textvariable=init_bal_text, width=20)
e4.grid(row=0,column=3)

monthly_deposit_text=StringVar()
e5=Entry(window,textvariable=monthly_deposit_text, width=20)
e5.grid(row=1,column=3)

# display listbox and attached a Scrollbar
list1=Listbox(window, height=12, width=90)
list1.grid(row=3, column=0, rowspan = 6, columnspan= 4 ) # we want to span across multiple rows and columns

sb1 = Scrollbar(window)
sb1.grid(row=3, column=4, rowspan=6)

list1.configure(yscrollcommand = sb1.set)
sb1.configure(command = list1.yview)

# Button handlers
def clear_command():
    e1.delete(0, END)
    e2.delete(0, END)

    e3.configure(state=NORMAL)
    e3.delete(0, END)
    e3.configure(state=DISABLED)

    e4.delete(0, END)
    e5.delete(0, END)
    list1.delete(0, END)

def exit_command():
    if messagebox.askokcancel("Quit", "Do you really wish to quit?"):
        window.destroy()

def compute_command():
    balance = int(init_bal_text.get())
    monthly_rate = float(interest_rate_text.get()) / 12.0
    months = int(year_text.get()) * 12 

    for month in range(1, months + 1):
        interest = (balance * monthly_rate)
        balance = balance + interest + int(monthly_deposit_text.get())
        line = str(month) + " " + monthly_deposit_text.get() + " " + str(round(float(interest), 2)) + " " + str(round(balance, 2))
        list1.insert(END, line)

    e3.configure(state=NORMAL)
    e3.insert(0, str(round(balance, 2)))
    e3.configure(state=DISABLED)
    




# Display Buttons
b1=Button(window, text="Compute", width=25, command=compute_command)
b1.grid(row=3, column=5)
b2=Button(window, text="Clear", width=25, command=clear_command)
b2.grid(row=4, column=5)
b3=Button(window, text="Exit", width=25, command=exit_command)
b3.grid(row=5, column=5)

window.mainloop()