from tkinter import *


# -------- Background ------------
window = Tk()
window.geometry("512x512")
window.title("Tic Tac Toe")
window.iconbitmap("images/2911080.ico")

# -------- Turn Text -------------
turn_label = Label(text="Turn: ")
turn_label.place(x=240, y=30)

turn_symbol = Label(text="O")
turn_symbol.place(x=270, y=30)

# ---------- Restart Button ------
restart_button = Button(text="Restart")
restart_button.place(x=240, y=50)

# ---------- Player Button -------
button1 = Button(text="O", height=7, width=23)
button1.place(x=0, y=100)
button2 = Button(text="X", height=7, width=23)
button2.place(x=180, y=100)
button3 = Button(text="O", height=7, width=23)
button3.place(x=360, y=100)
button4 = Button(text="X", height=7, width=23)
button4.place(x=0, y=230)
button5 = Button(text="O", height=7, width=23)
button5.place(x=180, y=230)
button6 = Button(text="O", height=7, width=23)
button6.place(x=360, y=230)
button7 = Button(text="X", height=7, width=23)
button7.place(x=0, y=360)
button8 = Button(text="O", height=7, width=23)
button8.place(x=180, y=360)
button9 = Button(text="X", height=7, width=23)
button9.place(x=360, y=360)








window.mainloop()