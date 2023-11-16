import tkinter as tk 
from  tkinter.font import Font

root= tk.Tk()
root.title("Calculator")
root.geometry("300x275")

calculation= ""
def addTocalculation(symbol):
    global calculation
    calculation+= str (symbol)
    textResult.delete(1.0, "end")
    textResult.insert(1.0, calculation)
def evaluateCalculation():
    global calculation
    try:
        calculation=str(eval(calculation))
        textResult.delete(1.0,"end")
        textResult.insert(1.0, calculation)
    except:
        clearField()
        textResult.insert(1.0, "Error")
def clearField():
    global calculation
    calculation=""
    textResult.delete(1.0,"end")


textResult= tk.Text(root, height=2 , width=16, font=("Arial" ,24))
textResult.grid(columnspan=5)

btn1=tk.Button(root, text="1", command=lambda: addTocalculation(1),width=5,font= ("Arial"))
btn1.grid(row=2,column=1)

btn2=tk.Button(root, text="2", command=lambda: addTocalculation(2),width=5,font= ("Arial"))
btn2.grid(row=2,column=2)

btn3=tk.Button(root, text="3", command=lambda: addTocalculation(3),width=5,font= ("Arial"))
btn3.grid(row=2,column=3)

btn4=tk.Button(root, text="4", command=lambda: addTocalculation(4),width=5,font= ("Arial"))
btn4.grid(row=3,column=1)

btn5=tk.Button(root, text="5", command=lambda: addTocalculation(5),width=5,font= ("Arial"))
btn5.grid(row=3,column=2)

btn6=tk.Button(root, text="6", command=lambda: addTocalculation(6),width=5,font= ("Arial"))
btn6.grid(row=3,column=3)

btn7=tk.Button(root, text="7", command=lambda: addTocalculation(7),width=5,font= ("Arial"))
btn7.grid(row=4,column=1)

btn8=tk.Button(root, text="8", command=lambda: addTocalculation(8),width=5,font= ("Arial"))
btn8.grid(row=4,column=2)

btn9=tk.Button(root, text="9", command=lambda: addTocalculation(9),width=5,font= ("Arial"))
btn9.grid(row=4,column=3)

btn0=tk.Button(root, text="0", command=lambda: addTocalculation(0),width=5,font= ("Arial"))
btn0.grid(row=5,column=2)

btnPlus=tk.Button(root, text="+", command=lambda: addTocalculation("+"),width=5,font= ("Arial"))
btnPlus.grid(row=2,column=4)

btnMinus=tk.Button(root, text="-", command=lambda: addTocalculation("-"),width=5,font= ("Arial"))
btnMinus.grid(row=3,column=4)

btnMul=tk.Button(root, text="*", command=lambda: addTocalculation("*"),width=5,font= ("Arial"))
btnMul.grid(row=4,column=4)

btnDiv=tk.Button(root, text="/", command=lambda: addTocalculation("/"),width=5,font= ("Arial"))
btnDiv.grid(row=5,column=4)

btnOpen=tk.Button(root, text="(", command=lambda: addTocalculation("("),width=5,font= ("Arial"))
btnOpen.grid(row=5,column=1)

btnClose=tk.Button(root, text=")", command=lambda: addTocalculation(")"),width=5,font= ("Arial"))
btnClose.grid(row=5,column=3)

btnClear=tk.Button(root, text="C", command=clearField,width=5,font= ("Arial"))
btnClear.grid(row=6,column=3)

btnEquals=tk.Button(root, text="=", command=evaluateCalculation, width=5,font= ("Arial"))
btnEquals.grid(row=6,column=1 , columnspan=2)

root.mainloop()