
from  tkinter import * 
from  tkinter.font import Font

root= Tk()
root.title("To-Do List")
root.geometry("500x500")
#root.resizable(False,False)

task_list=[]

myFont= Font (
    size= 25,
    weight="bold")

myFrame = Frame(root)
myFrame.pack(pady=10)

myList = Listbox(myFrame,
                 font=myFont,
                 width=25,
                 height=5,
                 bg="SystemButtonFace",
                 bd=0,
                 fg="#464646",
                 highlightthickness=0,
                 selectbackground="#a6a6a6",
                 activestyle="none"
                 )
myList.pack(side=LEFT, fill=BOTH)
stuff=[]
for item in stuff:
    myList.insert(END, item)

myScrollbar= Scrollbar(myFrame)
myScrollbar.pack(side=RIGHT, fill=BOTH)

myList.config(yscrollcommand=myScrollbar.set)
myScrollbar.config(command=myList.yview)


myEntry = Entry(root, font =("Helvetica",24))
myEntry.pack(pady=20)

buttonFrame= Frame(root)
buttonFrame.pack(pady=20)

#functions
def deleteItem():
    myList.delete(ANCHOR)
def addItem():
    myList.insert(END,myEntry.get())
    myEntry.delete(0,END)
def crossOffItem():
    myList.itemconfig(
        myList.curselection(),
        fg="#dedede"
    )
    myList.selection_clear(0,END)


def unCrossItem():
    myList.itemconfig(
        myList.curselection(),
        fg="#464646"
    )
    myList.selection_clear(0,END)
def deleteCrossed():
    count=0
    while count < myList.size():
        if myList.itemcget(count, "fg") == "#dedede":
            myList.delete(myList.index(count))
        else :
          count +=1


deleteButton = Button(buttonFrame,text="Delete Item", command=deleteItem)
addButton = Button(buttonFrame,text="Add Item", command=addItem)
crossOffButton = Button(buttonFrame,text="Cross-Off Item", command=crossOffItem)
uncrossButton = Button(buttonFrame,text="Uncross Item", command=unCrossItem)
deleteCrossedButton = Button(buttonFrame,text="Delete Crossed Item",command=deleteCrossed)

deleteButton.grid(row=0,column=0)
addButton.grid (row=0,column=1, padx=20)
crossOffButton.grid (row=0,column=2)
uncrossButton.grid (row=0,column=3,padx=20)
deleteCrossedButton.grid(row=0,column=4)

root.mainloop()