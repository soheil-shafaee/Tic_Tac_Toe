from tkinter import *

COUNT = 0
CLICK = True

# -------- Background ------------
window = Tk()
window.geometry("512x512")
window.title("Tic Tac Toe")
window.iconbitmap("images/2911080.ico")
window.configure(bg="#85adad")
window.resizable(False, False)

# -------- Turn Text -------------
turn_label = Label(text="Turn: ", bg="#85adad")
turn_label.place(x=240, y=30)

turn_symbol = Label(text="O", bg="#85adad")
turn_symbol.place(x=270, y=30)

# ---------- Restart Button ------
restart_button = Button(text="Restart")
restart_button.place(x=240, y=50)

# --------- Game Button ----------
btn1 = StringVar()
btn2 = StringVar()
btn3 = StringVar()
btn4 = StringVar()
btn5 = StringVar()
btn6 = StringVar()
btn7 = StringVar()
btn8 = StringVar()
btn9 = StringVar()

# --------- Image Section ---------
o_photo = PhotoImage(file="images/o.png")
x_photo = PhotoImage(file="images/x.png")


# --------- Game Play Section -----
def play():
    button1 = Button(window, height=7,
                     width=23,
                     relief="ridge",
                     borderwidth=.5,
                     textvariable=btn1,
                     command=lambda: press(1, 0, 100))
    button1.place(x=0, y=100)
    button2 = Button(window, height=7,
                     width=23,
                     relief="ridge",
                     borderwidth=.5,
                     textvariable=btn2,
                     command=lambda: press(2, 180, 100))
    button2.place(x=180, y=100)
    button3 = Button(window, height=7,
                     width=23,
                     relief="ridge",
                     borderwidth=.5,
                     textvariable=btn3,
                     command=lambda: press(3, 360, 100))
    button3.place(x=360, y=100)
    button4 = Button(window, height=7,
                     width=23,
                     relief="ridge",
                     borderwidth=.5,
                     textvariable=btn4,
                     command=lambda: press(4, 0, 230))
    button4.place(x=0, y=230)
    button5 = Button(window, height=7,
                     width=23,
                     relief="ridge",
                     borderwidth=.5,
                     textvariable=btn5,
                     command=lambda: press(5, 180, 230))
    button5.place(x=180, y=230)
    button6 = Button(window, height=7,
                     width=23,
                     relief="ridge",
                     borderwidth=.5,
                     textvariable=btn6,
                     command=lambda: press(6, 360, 230))
    button6.place(x=360, y=230)
    button7 = Button(window, height=7,
                     width=23,
                     relief="ridge",
                     borderwidth=.5,
                     textvariable=btn7,
                     command=lambda: press(7, 0, 360))
    button7.place(x=0, y=360)
    button8 = Button(window, height=7,
                     width=23,
                     relief="ridge",
                     borderwidth=.5,
                     textvariable=btn8,
                     command=lambda: press(8, 180, 360))
    button8.place(x=180, y=360)
    button9 = Button(window, height=7,
                     width=23,
                     relief="ridge",
                     borderwidth=.5,
                     textvariable=btn9,
                     command=lambda: press(9, 360, 360))
    button9.place(x=360, y=360)


play()


def press(num, r, c):
    global CLICK, COUNT

    if CLICK:
        label_image = Label(window, image=x_photo)
        if num == 1:
            btn1.set("x")
        elif num == 2:
            btn2.set("x")
        elif num == 3:
            btn2.set("x")
        elif num == 4:
            btn4.set("x")
        elif num == 5:
            btn5.set("x")
        elif num == 6:
            btn6.set("x")
        elif num == 7:
            btn7.set("x")
        elif num == 8:
            btn8.set("x")
        else:
            btn9.set("x")
        COUNT += 1
        label_image.place(x=r, y=c)
        CLICK = False
    else:
        label_image = Label(window, image=o_photo)
        if num == 1:
            btn1.set("o")
        elif num == 2:
            btn2.set("o")
        elif num == 3:
            btn2.set("o")
        elif num == 4:
            btn4.set("o")
        elif num == 5:
            btn5.set("o")
        elif num == 6:
            btn6.set("o")
        elif num == 7:
            btn7.set("o")
        elif num == 8:
            btn8.set("o")
        else:
            btn9.set("o")
        COUNT += 1
        label_image.place(x=r, y=c)
        CLICK = True


def win_check():
    pass


# --------- Display Section --------
window.mainloop()
