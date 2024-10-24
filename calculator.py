def ok(ca):
    global lhs, op
    bind = ca.widget
    str = bind.cget("text")
    if str == "+" or str == "-" or str == "*" or str == '/':
         op = str
         lhs = float(E.get())
         E.delete(0, END)
         E.focus()
    elif str == "=":
        rhs = float(E.get())
        E.delete(0, END)
        if op == "+":
              to = lhs+rhs
        if op == "-":
              to = lhs-rhs
        if op == "*":
              to = lhs*rhs
        if op == '/':
              to = lhs / rhs
              to = float("%.2f"%to)
        E.insert(END, to)
    else:
         E.insert(END, str)

def clear():
    E.delete(0, END)
    E.focus()


from tkinter import *
top = Tk()
top.geometry("250x300+1100+100")
top.maxsize(250, 300)
top.minsize(250, 300)
top.title("Calculator.app")
top["background"] = "Grey"
E = Entry(font=("Times", 18), width=16, borderwidth=5)
b1 = Button(text="1", font="Times,16", activebackground="Pink", width=3, borderwidth=6)
b2 = Button(text="2", font="Times,16", activebackground="Pink", width=3, borderwidth=6)
b3 = Button(text="3", font="Times,16", activebackground="Pink", width=3, borderwidth=6)
b4 = Button(text="4", font="Times,16", activebackground="Pink", width=3, borderwidth=6)
b5 = Button(text="5", font="Times,16", activebackground="Pink", width=3, borderwidth=6)
b6 = Button(text="6", font="Times,16", activebackground="Pink", width=3, borderwidth=6)
b7 = Button(text="7", font="Times,16", activebackground="Pink", width=3, borderwidth=6)
b8 = Button(text="8", font="Times,16", activebackground="Pink", width=3, borderwidth=6)
b9 = Button(text="9", font="Times,16", activebackground="Pink", width=3, borderwidth=6)
b10 = Button(text="0", font="Times,16", activebackground="Pink", width=3, borderwidth=6)
b12 = Button(text="C", font=("Times", 15), activebackground="Pink", width=3, borderwidth=6, command=clear)
b13 = Button(text="+", font=("Times", 15), activebackground="Pink", width=3, borderwidth=6)
b14 = Button(text="*", font=("Times", 15), activebackground="Pink", width=3, borderwidth=6)
b15 = Button(text="/", font=("Times", 15), activebackground="Pink", width=3, borderwidth=6)
b16 = Button(text="-", font=("Times", 15), activebackground="Pink", width=3, borderwidth=6)
b17 = Button(text="=", font=("Times", 15), activebackground="Pink", width=3, borderwidth=6)
E.pack(pady=10)
b1.bind('<Button-1>', ok)
b2.bind('<Button-1>', ok)
b3.bind('<Button-1>', ok)
b4.bind('<Button-1>', ok)
b5.bind('<Button-1>', ok)
b6.bind('<Button-1>', ok)
b7.bind('<Button-1>', ok)
b8.bind('<Button-1>', ok)
b9.bind('<Button-1>', ok)
b10.bind('<Button-1>', ok)
b13.bind('<Button-1>', ok)
b14.bind('<Button-1>', ok)
b15.bind('<Button-1>', ok)
b17.bind('<Button-1>', ok)
b16.bind('<Button-1>', ok)
b7.place(x=23, y=66)
b8.place(x=76, y=66)
b9.place(x=129, y=66)
b4.place(x=23, y=116)
b5.place(x=76, y=116)
b6.place(x=129, y=116)
b1.place(x=23, y=167)
b2.place(x=76, y=167)
b3.place(x=129, y=167)
b10.place(x=76, y=218)
b12.place(x=23, y=218)
b17.place(x=129, y=218)
b13.place(x=188, y=66)
b14.place(x=188, y=116)
b15.place(x=188, y=167)
b16.place(x=188, y=218)
top.mainloop()