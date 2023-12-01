from tkinter import *
import random

# num = StringVar()


def generate_numbers():
    lot_nums = set()

    while len(lot_nums) < 6:
        lot_nums.add(random.randrange(1, 60))

    numbers_string.set(str(lot_nums))
    button_text.set("Generate More Numbers")


# def launch_app():
root = Tk()

root.geometry("420x140")
frame = Frame(root, bd=5, bg="white")
frame.pack()

numbers_string = StringVar()
numbers_string.set(">> Your numbers will appear here <<")

button_text = StringVar()
button_text.set("Generate Numbers")

# app_name_label = Label(frame, text="Lottery Number Selector")
# app_name_label.pack()

numbers_label = Label(
    frame,
    textvariable=numbers_string,
    bg="yellow",
    fg="green",
    height=3,
    width=100,
    font="Tahoma 16 bold",
)
numbers_label.pack()

button = Button(
    frame,
    textvariable=button_text,
    command=generate_numbers,
    font="Tahoma 14 bold",
    bd=2,
    bg="green",
    fg="gold",
    relief="groove",
    width=80,
)
button.pack(padx=5, pady=5)

root.title("Lottery Number Selector")
root.mainloop()


# launch_app()
