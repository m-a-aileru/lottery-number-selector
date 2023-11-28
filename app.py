from tkinter import *
import random


def output():
    lot_nums = set()

    while len(lot_nums) < 6:
        lot_nums.add(random.randrange(1, 60))

    print(lot_nums)


def launch_app():
    root = Tk()
    root.geometry("640x480")
    frame = Frame(root, bd=5, bg="purple")
    frame.pack()

    midframe = Frame(root, bg="blue", bd=3)
    midframe.pack(side=BOTTOM)

    label = Label(frame, text="Lottery Number Selector")
    label.pack()

    button = Button(
        midframe,
        text="Generate Numbers",
        command=output,
        fg="green",
        font="Verdana 12 bold",
        bd=2,
        bg="light blue",
        relief="groove",
    )
    button.pack(padx=5, pady=5)

    root.title("Lottery Number Selector")
    root.mainloop()


launch_app()
