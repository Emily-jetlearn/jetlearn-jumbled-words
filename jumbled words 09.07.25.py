from tkinter import *
import random
from tkinter import messagebox
window=Tk()
window.geometry("600x600")
window.title("Jumbled word game")
window.config(bg="#c3e6c7")

correct=["night","horse","sinister","moon","Tokyo"]
jumbled=["tghin","sreoh","stinersi","onom","oTyko"]
num=random.randrange(0,len(jumbled),1)
anscount=0
totalatmp=0
score=""
display_score=Label(window)

Label(window,text="Jumbled word game").pack()
game_word=Label(window)
game_word.pack(pady=20,ipadx=5,ipady=5)

window.mainloop()



