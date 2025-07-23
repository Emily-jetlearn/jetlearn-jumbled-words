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
display_score.pack(pady=20,ipadx=5,ipady=5)

def reset():
    global jumbled,correct,num
    num=random.randrange(0,len(jumbled),1)
    game_word.config(text=jumbled[num])
    guess.delete(0,END)

def default_settings():
    global jumbled,correct,num
    game_word.config(text=jumbled[num])

def check():
    global jumbled,correct,num,anscount,totalatmp,score,display_score
    totalatmp=int(totalatmp)+1
    var=guess.get()
    if var == correct[num]:
        messagebox.showinfo("info","Correct answer, well done!")
        anscount=int(anscount) + 1
        
        totalatmp=int(totalatmp) + 1             

    else:
        messagebox.showinfo("info","Sorry, wrong answer")
        totalatmp=int(totalatmp) + 1

    score="Your score: " + str(anscount)

    display_score.forget()
    display_score=Label(window,text=score)
    display_score.pack(side=LEFT,pady=20,ipadx=5,ipady=5)
    reset()




Label(window,text="Jumbled word game",fg="#e7bbfb",font= 18).pack()
game_word=Label(window)
game_word.pack(pady=20,ipadx=5,ipady=5)
answer=StringVar()
guess=Entry(window,width=30,textvariable=answer)
guess.pack(pady=20,ipadx=5,ipady=5)
resetbutton=Button(window,text="Reset",fg="#8c6e8f",bg="#c0c8ed",command=reset)
resetbutton.pack(pady=20,ipadx=5,ipady=5)
checkbutton=Button(window,text="Check",fg="#8c6e8f",bg="#c0c8ed",command=check)
checkbutton.pack(pady=20,ipadx=5,ipady=5)
default_settings()



window.mainloop()



