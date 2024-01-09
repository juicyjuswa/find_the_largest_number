# import tkinter module
import tkinter as tk
from tkinter import *

# root window
root = tk.Tk()
root.geometry ("485x215")
# title and background of the window
root.title("Find The Largest Number")
root.config(bg="black")

# Ask user to input four(4) numbers
first_number = Label (root, text = "Enter the first number: ", fg="lime", bg="black")
first_number.place(x = 50, y = 20)
first_entry = tk.Entry(root, fg="lime", bg="black", insertbackground="lime")
first_entry.place (x = 230, y = 20 , width = 200)

second_number = Label (root, text = "Enter the second number: ", fg="lime", bg="black")
second_number.place (x = 50, y = 50)
second_entry = tk.Entry(root, fg="lime", bg="black", insertbackground="lime")
second_entry.place (x = 230, y = 50 , width = 200)

third_number = Label (root, text = "Enter the third number: ", fg="lime", bg="black")
third_number.place (x = 50, y = 80)
third_entry = tk.Entry(root, fg="lime", bg="black", insertbackground="lime")
third_entry.place (x = 230, y = 80 , width = 200)

fourth_number = Label (root, text = "Enter the fourth number: ", fg="lime", bg="black")
fourth_number.place (x = 50, y = 110)
fourth_entry = tk.Entry(root, fg="lime", bg="black", insertbackground="lime")
fourth_entry.place (x = 230, y = 110 , width = 200)


# results
label = tk.Label(root, fg="lime", bg="black")

#function for largest number
def find_the_largest_number():
    # values from input users
    try:
        integer_1 = int(first_entry.get())
        integer_2 = int(second_entry.get())
        integer_3 = int(third_entry.get())
        integer_4 = int(fourth_entry.get())
    except ValueError:
        # no using of alphabets
        label.config(text="Please enter valid numbers", fg="lime", bg="black")
        return
    # check integer_1
    if integer_1 >= integer_2 and integer_1 >= integer_3 and integer_1 >= integer_4:
        biggest_number = integer_1
    # check integer_2
    elif integer_2 >= integer_1 and integer_2 >= integer_3 and integer_2 >= integer_4:
        biggest_number = integer_2
    # check integer_3
    elif integer_3 >= integer_1 and integer_3 >= integer_2 and integer_3 >= integer_4:
        biggest_number = integer_3
    # check integer_4
    else:
        biggest_number = integer_4
    # display the largest number
    label.config(text=f"The largest number is {biggest_number}", fg="lime", bg="black")

# function trigger button
button = tk.Button(root, text="Find", 
  command=find_the_largest_number,
  fg="lime", bg="black", activebackground="lime",
  activeforeground="lime")

button.place(x = 101, y = 160)
label.place(x = 180, y = 160, width = 250)

# start the main loop
root.mainloop()
