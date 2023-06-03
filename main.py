import tkinter.messagebox
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

turn_symbol = Label(text="x", bg="#85adad")
turn_symbol.place(x=270, y=30)

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
        turn_symbol.config(text="O")
        if num == 1:
            btn1.set("x")
        elif num == 2:
            btn2.set("x")
        elif num == 3:
            btn3.set("x")
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
        win_check()
    else:
        label_image = Label(window, image=o_photo)
        turn_symbol.config(text="X")
        if num == 1:
            btn1.set("o")
        elif num == 2:
            btn2.set("o")
        elif num == 3:
            btn3.set("o")
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
        win_check()


def win_check():
    global CLICK, COUNT
    if (btn1.get() == "x" and btn2.get() == "x" and btn3.get() == "x"
            or btn4.get() == "x" and btn5.get() == "x" and btn6.get() == "x"
            or btn7.get() == "x" and btn8.get() == "x" and btn9.get() == "x"
            or btn1.get() == "x" and btn4.get() == "x" and btn7.get() == "x"
            or btn2.get() == "x" and btn5.get() == "x" and btn8.get() == "x"
            or btn3.get() == "x" and btn6.get() == "x" and btn9.get() == "x"
            or btn1.get() == "x" and btn5.get() == "x" and btn9.get() == "x"
            or btn3.get() == "x" and btn5.get() == "x" and btn7.get() == "x"):
        tkinter.messagebox.showinfo("Tic Tac Toe", "The Player 'x' Win!")
        CLICK = True
        COUNT = 0
        play()
    elif (btn1.get() == "o" and btn2.get() == "o" and btn3.get() == "o"
          or btn4.get() == "o" and btn5.get() == "o" and btn6.get() == "o"
          or btn7.get() == "o" and btn8.get() == "o" and btn9.get() == "o"
          or btn1.get() == "o" and btn4.get() == "o" and btn7.get() == "o"
          or btn2.get() == "o" and btn5.get() == "o" and btn8.get() == "o"
          or btn3.get() == "o" and btn6.get() == "o" and btn9.get() == "o"
          or btn1.get() == "o" and btn5.get() == "o" and btn9.get() == "o"
          or btn3.get() == "o" and btn5.get() == "o" and btn7.get() == "o"):
        tkinter.messagebox.showinfo("Tic Tac Toe", "The Player 'O' Win!")
        CLICK = True
        COUNT = 0
    elif COUNT == 9:
        tkinter.messagebox.showinfo("Tic Tac Toe", "Tie Game!!")
        CLICK = True
        COUNT = 0


def clear():
    btn1.set("")
    btn2.set("")
    btn3.set("")
    btn4.set("")
    btn5.set("")
    btn6.set("")
    btn7.set("")
    btn8.set("")
    btn9.set("")
    play()


# ---------- Restart Button ------
restart_button = Button(text="Restart", command=clear)
restart_button.place(x=240, y=50)

# --------- Display Section --------
window.mainloop()
