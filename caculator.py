import tkinter as tk

caculation=""

def add(symbol):
    global caculation 
    caculation+=str(symbol)
    text_result.delete(1.0,"end")
    text_result.insert(1.0,caculation)
def evul():
    global caculation
    try:
        caculation=str(eval(caculation))
        text_result.delete(1.0,"end")
        text_result.insert(1.0,caculation)
    except:
        clear_field()
        text_result.insert(1.0,"Error")
def clear_field():
    global caculation
    caculation=""
    text_result.delete(1.0,"end")


root=tk.Tk() 
root.geometry("300x300")
text_result = tk.Text(root,height=2,width=20,font=("Arial",20))
text_result.grid(columnspan=5)

bt1 =tk.Button(root, text="1",command=lambda: add(1),width=5,font=("Arial",16))
bt1.grid(row=2,column=1)
bt2 =tk.Button(root, text="2",command=lambda: add(2),width=5,font=("Arial",16))
bt2.grid(row=2,column=2)
bt3 =tk.Button(root, text="3",command=lambda: add(3),width=5,font=("Arial",16))
bt3.grid(row=2,column=3)
bt4 =tk.Button(root, text="4",command=lambda: add(4),width=5,font=("Arial",16))
bt4.grid(row=3,column=1)
bt5 =tk.Button(root, text="5",command=lambda: add(5),width=5,font=("Arial",16))
bt5.grid(row=3,column=2)
bt6 =tk.Button(root, text="6",command=lambda: add(6),width=5,font=("Arial",16))
bt6.grid(row=3,column=3)
bt7 =tk.Button(root, text="7",command=lambda: add(7),width=5,font=("Arial",16))
bt7.grid(row=4,column=1)
bt8 =tk.Button(root, text="8",command=lambda: add(8),width=5,font=("Arial",16))
bt8.grid(row=4,column=2)
bt9 =tk.Button(root, text="9",command=lambda: add(9),width=5,font=("Arial",16))
bt9.grid(row=4,column=3)
bt0 =tk.Button(root, text="0",command=lambda: add(0),width=5,font=("Arial",16))
bt0.grid(row=5,column=1)
btpl =tk.Button(root, text="+",command=lambda: add('+'),width=5,font=("Arial",16))
btpl.grid(row=2,column=4)
btmn =tk.Button(root, text="-",command=lambda: add('-'),width=5,font=("Arial",16))
btmn.grid(row=3,column=4)
btmul =tk.Button(root, text="*",command=lambda: add('*'),width=5,font=("Arial",16))
btmul.grid(row=4,column=4)
btdiv =tk.Button(root, text="/",command=lambda: add('/'),width=5,font=("Arial",16))
btdiv.grid(row=5,column=4)
btdop =tk.Button(root, text="(",command=lambda: add('('),width=5,font=("Arial",16))
btdop.grid(row=5,column=2)
btdcl =tk.Button(root, text=")",command=lambda: add(')'),width=5,font=("Arial",16))
btdcl.grid(row=5,column=3)
bteq =tk.Button(root, text="=",command=evul,width=11,font=("Arial",16))
bteq.grid(row=6,column=3,columnspan=2)
btcl =tk.Button(root, text="AC",command=clear_field,width=11,font=("Arial",16))
btcl.grid(row=6,column=1,columnspan=2)

root.mainloop()
