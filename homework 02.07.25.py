from tkinter import *
from tkinter.filedialog import *
from tkinter import messagebox
window=Tk()
window.geometry("900x900")


def delfile():
    index=remember.get(ANCHOR)
    if index:
        remember.delete(ANCHOR)
        quoteadd.remove(index)
    else:
        messagebox.showwarning("ERROR","could not delete file")

def addfile():
    newquote=listadd.get().strip()
    if newquote and newquote not in quoteadd:
        quoteadd.append(newquote)
        remember.insert(END,newquote)
        listadd.delete(0,END)
    else:
        messagebox.showwarning("ERROR","invalid input")


f1=Frame(window)
f1.pack(pady=10,padx=15)
scroll=Scrollbar(f1,orient="vertical")
remember=Listbox(f1,width=50,yscrollcommand=scroll.set,selectmode=SINGLE)
remember.pack(pady=10)
quoteadd=["a blessing in disgiuse","a dime a dozen","beat around the bush","better late than never"]
listadd=Entry(f1,width=50)
listadd.pack(pady=10)
addbutton=Button(f1,text="add a quote",command=addfile)
addbutton.pack(pady=10)
delbutton=Button(f1,text="delete a quote", command=delfile)
delbutton.pack(pady=10)
for i in quoteadd:
    remember.insert(END, i)

def plan():
    plan1=activity.get()
    plan2=excite_level.get()
    plan3=time.get()
    Plan.config(text=f"activityselected {plan1} \n excite_levelselected {plan2} \n timeselected {plan3}")


f2=Frame(window)
f2.pack(pady=40)
canactiv=Label(f2,text="Choose an activity: ")
canactiv.grid(row=0,column=0,padx=20,pady=20)
activity=Spinbox(f2,values=("movie marathon","slumber party","Quiz night","Game night","Hiking","Nature walk"))
activity.grid(row=0,column=1,padx=20,pady=20)
Excitement=Label(f2,text="Rate your excitement: ")
Excitement.grid(row=1,column=0,padx=20,pady=20)
excite_level=Spinbox(f2,from_=0 , to=11 , increment=0.1)
excite_level.grid(row=1,column=1,padx=20,pady=20)
Time_spent=Label(f2,text="How long?: ")
Time_spent.grid(row=2,column=0,padx=20,pady=20)
time=Spinbox(f2, from_=1 ,to=6)
time.grid(row=2,column=1,padx=20,pady=20)
show_plan=Button(f2,text="Show plan",command=plan)
show_plan.grid(row=3,column=1,padx=20,pady=20)
Plan=Label(f2,text="Your plan is:")
Plan.grid(row=4,column=1)


window.mainloop()