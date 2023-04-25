from tkinter import *
import pyglet


# ------- Background UI ---------------
window = Tk()
window.iconbitmap('images/2911080.ico')
window.title(string="Tic Tac Toe")
pyglet.font.add_file("fonts/RubikPixels-Regular.ttf")
window.geometry("512x512")
text = Label(text="Tic Tac Toe",
             font=("RubikPixels-Regular", 30, "bold"),
             fg="blue")
text.place(x=100, y=100)




window.mainloop()
