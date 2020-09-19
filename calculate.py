# Importing all classes / Functions
#from the tkinter
from tkinter import *


# Functions to clear the content of all entry boxes

def clear_all():
    principle_field.delete(0, End)
    rate_field.delete(0, End)
    time_field.delete(0, End)
    compound.field.delete(0, End)


# Focus on prinicple_field entry box
#principle.field.focus_set()

# Function to find compound interest

def calculate_ci():
    # get content from entry Box
    principle = int(principle_field.get())

    rate = float(rate_field.get())

    time = int(time_field.get())

    # calculate compound Interest
    CI = principle * (pow((1 + rate / 100), time))

    # insert method inserting value to the text entry
    compound_field.insert(10, CI)


# create GUI window
root = Tk()

# set background color
root.configure(background='black')

# set geometry for GUI window
root.geometry("500x600")

# set title for GUI
root.title("Compound Interest Calculator")

# creating Principle amount = Label
label1 = Label(root, text="Principle Amount(EUR) : ", fg='white', bg='green')

# creating Rate = Label
label2 = Label(root, text="Rate(%) : ", fg='white', bg='green')

# Creating Time = Label
label3 = Label(root, text="Time(years) : ", fg='white', bg='green')

# create Compund Interest = Label
label4 = Label(root, text="Compound Interest : ", fg='white', bg='green')

# using Grid / padx / pady

label1.grid(row=1, column=0, padx=10, pady=10)
label2.grid(row=2, column=0, padx=10, pady=10)
label3.grid(row=3, column=0, padx=10, pady=10)
label4.grid(row=5, column=0, padx=10, pady=10)


# creating entry box for Info
principle_field = Entry(root)
rate_field = Entry(root)
time_field = Entry(root)
compound_field = Entry(root)

# placing entry box using Grid/ padx / pady

principle_field.grid(row=1, column=1, padx=10, pady=10)
rate_field.grid(row=2, column=1, padx=10, pady=10)
time_field.grid(row=3, column=1, padx=10, pady=10)
compound_field.grid(row=5, column=1, padx=10, pady=10)

# creating submit Button + calculate CI
button1 = Button(root, text="Submit", fg='white', bg='green', command=calculate_ci)

# creating a clear button
button2 = Button(root, text="Clear", fg='white', bg='green', command=clear_all)

# placing buttons using Grid
button1.grid(row=4, column=1, pady=10)
button2.grid(row=6, column=1, pady=10)

root.mainloop()
