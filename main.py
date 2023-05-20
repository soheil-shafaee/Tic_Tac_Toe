from tkinter import *

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
O_photo = PhotoImage(file="images/o.png")
x_photo = PhotoImage(file="images/x.png")


# --------- Game Play Section -----
def play():
    button1 = Button(window, height=7,
                     width=23,
                     relief="ridge",
                     borderwidth=.5,
                     textvariable=btn1)
    button1.place(x=0, y=100)
    button2 = Button(window, height=7,
                     width=23,
                     relief="ridge",
                     borderwidth=.5,
                     textvariable=btn2)
    button2.place(x=180, y=100)
    button3 = Button(window, height=7,
                     width=23,
                     relief="ridge",
                     borderwidth=.5,
                     textvariable=btn3)
    button3.place(x=360, y=100)
    button4 = Button(window, height=7,
                     width=23,
                     relief="ridge",
                     borderwidth=.5,
                     textvariable=btn4)
    button4.place(x=0, y=230)
    button5 = Button(window, height=7,
                     width=23,
                     relief="ridge",
                     borderwidth=.5,
                     textvariable=btn5)
    button5.place(x=180, y=230)
    button6 = Button(window, height=7,
                     width=23,
                     relief="ridge",
                     borderwidth=.5,
                     textvariable=btn6)
    button6.place(x=360, y=230)
    button7 = Button(window, height=7,
                     width=23,
                     relief="ridge",
                     borderwidth=.5,
                     textvariable=btn7)
    button7.place(x=0, y=360)
    button8 = Button(window, height=7,
                     width=23,
                     relief="ridge",
                     borderwidth=.5,
                     textvariable=btn8)
    button8.place(x=180, y=360)
    button9 = Button(window, height=7,
                     width=23,
                     relief="ridge",
                     borderwidth=.5,
                     textvariable=btn9)
    button9.place(x=360, y=360)


play()


def press(num, r, c):
    pass


# --------- Display Section --------
window.mainloop()
