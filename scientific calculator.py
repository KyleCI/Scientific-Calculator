from tkinter import *
import math
import tkinter.messagebox
import parser

switch = None

# Getting user input
i = 0


def get_variables(num):
    global i
    j = display.get()
    if j == "0":
        clear_all()
        display.insert(0, num)
    else:
        display.insert(i, num)
        i += 1


def get_operation(operator):
    global i
    length = len(operator)
    display.insert(i, operator)
    i += length


def get_operation_minus(num2):
    j = display.get()
    if j == "0" or any(x in num2 for x in j):
        print("")
    else:
        clear_all()
        display.insert(0, num2 + j)


def get_operation_dot(num3):
    global i
    j = display.get()
    if any(x in num3 for x in j):
        print("")
    else:
        display.insert(i, num3)
        i += 1


def calculate():
    entire_string = display.get()
    try:
        a = parser.expr(entire_string).compile()
        result = eval(a)
        clear_all()
        display.insert(0, result)

    except Exception:
        clear_all()
        tkinter.messagebox.showerror("Value Error", "Result Undefined")


def clear_all():
    display.delete(0, END)


def undo():
    entire_string = display.get()
    if len(entire_string) > 0:
        new_string = entire_string[: -1]
        clear_all()
        display.insert(0, new_string)


def tan_clicked():
    try:
        ans = float(display.get())
        ans = math.tan(math.radians(ans))
        display.delete(0, END)
        display.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")


def cos_clicked():
    try:
        ans = float(display.get())
        ans = math.cos(math.radians(ans))
        display.delete(0, END)
        display.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")


def sin_clicked():
    try:
        ans = float(display.get())
        ans = math.sin(math.radians(ans))
        display.delete(0, END)
        display.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")


def conv_clicked():
    global switch
    if switch is None:
        switch = True
        conv_btn['text'] = "Deg"
    else:
        switch = None
        conv_btn['text'] = "Rad"


def fact_op():
    try:
        ans = float(display.get())
        ans = math.factorial(ans)
        display.delete(0, END)
        display.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")


def pi_op():
    j = display.get()
    num5 = float(math.pi)
    if j:
        clear_all()
        display.insert(0, float(j) * num5)
    else:
        display.insert(0, num5)


def log10_op():
    try:
        ans = float(display.get())
        ans = math.log10(ans)
        display.delete(0, END)
        display.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")


def log2_op():
    try:
        ans = float(display.get())
        ans = math.log2(ans)
        display.delete(0, END)
        display.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")


def log_op():
    try:
        ans = float(display.get())
        ans = math.log(ans)
        display.delete(0, END)
        display.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")


def sqr_op():
    try:
        ans = float(display.get())
        ans = math.sqrt(ans)
        display.delete(0, END)
        display.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check your values")


def ln_op():
    try:
        ans = float(display.get())
        ans = math.log(ans)
        display.delete(0, END)
        display.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("ln Error", "Check your values")


def e_op():
    if display.get() == '0':
        display.delete(0, END)
    pos = len(display.get())
    display.insert(pos, str(math.e))


def sin_inv():
    try:
        ans = float(display.get())
        ans = math.degrees(math.asin(ans))
        display.delete(0, END)
        display.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")


def cos_inv():
    try:
        ans = float(display.get())
        ans = math.degrees(math.acos(ans))
        display.delete(0, END)
        display.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")


def tan_inv():
    try:
        ans = float(display.get())
        ans = math.degrees(math.atan(ans))
        display.delete(0, END)
        display.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")


def round_op():
    try:
        ans = float(display.get())
        ans = round(ans)
        display.delete(0, END)
        display.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")


# Menufunctions
def Exit():
    Exit = tkinter.messagebox.askyesno("Scientific Calculator", "Confirm if you want to exit")
    if Exit > 0:
        root.destroy()
        return


def Exit2():
    Exit = tkinter.messagebox.askyesno("Scientific Calculator", "Confirm if you want to FUCK OFF!!")
    if Exit > 0:
        root.destroy()
        return


def Scientific():
    root.resizable(width=False, height=False)
    root.geometry("324x350+0+0")


def Standard():
    root.resizable(width=False, height=False)
    root.geometry("270x350+0+0")


root = Tk()
root.title("Scientific Calculator")
# root.configure(background = "white")
root.resizable(width=False, height=False)
# root.iconbitmap(True, "images/icon.ico")
root.geometry("270x350+0+0")

menubar = Menu(root)
root.config(menu=menubar)

filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Standard", command=Standard)
filemenu.add_command(label="Scientific", command=Scientific)

filemenu.add_separator()
filemenu.add_command(label="Exit", command=Exit)

editmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit", menu=editmenu)
editmenu.add_command(label="Copy")
editmenu.add_command(label="Paste")

editmenu.add_separator()
editmenu.add_command(label="Cut")

helpmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="Search")

helpmenu.add_separator()
helpmenu.add_command(label="Help")

# Passing the input field

display = Entry(root, relief=SUNKEN, bd=10, bg="white", width=15, justify=RIGHT, cursor="arrow")
display.grid(row=0, column=0, pady=0, columnspan=5, sticky=W + E)
# display.insert(0,"0")

# Adding buttons
Button(root, text="log", command=log_op, width=6, height=2, bd=3).grid(row=2, column=0, pady=1)
Button(root, text="cos", command=cos_clicked, width=6, height=2, bd=3).grid(row=2, column=1, pady=1)
Button(root, text="tan", command=tan_clicked, width=6, height=2, bd=3).grid(row=2, column=2, pady=1)
Button(root, text="sin", command=sin_clicked, width=6, height=2, bd=3).grid(row=2, column=3, pady=1)
Button(root, text="mod", command=lambda: get_operation("%"), width=6, height=2, bd=3).grid(row=2, column=4, pady=1)
Button(root, text="sin-1", command=sin_inv, width=6, height=2, bd=3).grid(row=2, column=5, pady=1)

Button(root, text="log10", command=log10_op, width=6, height=2, bd=3).grid(row=3, column=0, pady=1)
Button(root, text="log2", command=log2_op, width=6, height=2, bd=3).grid(row=3, column=1, pady=1)
conv_btn: None = Button(root, text="Deg", command=conv_clicked, width=6, height=2, bd=3).grid(row=3, column=2, pady=1)
Button(root, text="x^y", width=6, height=2, bd=3, command=lambda: get_operation("**")).grid(row=3, column=3, pady=1)
Button(root, text="√", command=sqr_op, width=6, bd=3, height=2).grid(row=3, column=4, pady=1)
Button(root, text="cos-1", command=cos_inv, bd=3, width=6, height=2).grid(row=3, column=5, pady=1)

Button(root, text=chr(177), width=6, height=2, bd=3, command=lambda: get_operation_minus("-")).grid(row=4, column=0,
                                                                                                    pady=1)
Button(root, text="CE", width=6, height=2, bg="red", bd=3).grid(row=4, column=1, pady=1)
Button(root, text="C", width=6, height=2, bd=3, bg="red", command=lambda: clear_all()).grid(row=4, column=2, pady=1)
Button(root, text="⌫", width=6, height=2, bd=3, bg="red", command=lambda: undo()).grid(row=4, column=3, pady=1)
Button(root, text=chr(247), width=6, height=2, bd=3, command=lambda: get_operation("/")).grid(row=4, column=4, pady=1)
Button(root, text="tan-1", command=tan_inv, bd=3, width=6, height=2).grid(row=4, column=5, pady=1)

Button(root, text="π", command=pi_op, width=6, height=2).grid(row=5, column=0, pady=1)
Button(root, text="7", width=6, height=2, bd=3, command=lambda: get_variables("7")).grid(row=5, column=1, pady=1)
Button(root, text="8", width=6, height=2, bd=3, command=lambda: get_variables("8")).grid(row=5, column=2, pady=1)
Button(root, text="9", width=6, height=2, bd=3, command=lambda: get_variables("9")).grid(row=5, column=3, pady=1)
Button(root, text="x", width=6, height=2, bd=3, command=lambda: get_operation("*")).grid(row=5, column=4, pady=1)
Button(root, text="e", command=e_op, width=6, height=2, bd=3).grid(row=5, column=5, pady=1)

Button(root, text="n!", width=6, height=2, bd=3, command=fact_op).grid(row=6, column=0, pady=1)
Button(root, text="4", width=6, height=2, bd=3, command=lambda: get_variables("4")).grid(row=6, column=1, pady=1)
Button(root, text="5", width=6, height=2, bd=3, command=lambda: get_variables("5")).grid(row=6, column=2, pady=1)
Button(root, text="6", width=6, height=2, bd=3, command=lambda: get_variables("6")).grid(row=6, column=3, pady=1)
Button(root, text="-", width=6, height=2, bd=3, command=lambda: get_operation("-")).grid(row=6, column=4, pady=1)
Button(root, text="ln", command=ln_op, width=6, height=2, bd=3).grid(row=6, column=5, pady=1)

Button(root, text="%", width=6, height=2, bd=3, command=lambda: get_operation("%")).grid(row=7, column=0, pady=1)
Button(root, text="1", width=6, height=2, bd=3, command=lambda: get_variables("1")).grid(row=7, column=1, pady=1)
Button(root, text="2", width=6, height=2, bd=3, command=lambda: get_variables("2")).grid(row=7, column=2, pady=1)
Button(root, text="3", width=6, height=2, bd=3, command=lambda: get_variables("3")).grid(row=7, column=3, pady=1)
Button(root, text="+", width=6, height=2, bd=3, command=lambda: get_operation("+")).grid(row=7, column=4, pady=1)
Button(root, text="round", command=round_op, width=6, height=2, bd=3).grid(row=7, column=5, pady=1)

Button(root, text="(", width=6, height=2, bd=3, command=lambda: get_operation("(")).grid(row=8, column=0, pady=1)
Button(root, text=")", width=6, height=2, bd=3, command=lambda: get_operation(")")).grid(row=8, column=1, pady=1)
Button(root, text="0", width=6, height=2, bd=3, command=lambda: get_variables("0")).grid(row=8, column=2, pady=1)
Button(root, text=".", width=6, height=2, bd=3, command=lambda: get_operation_dot(".")).grid(row=8, column=3, pady=1)
Button(root, text="=", width=6, height=2, bd=3, command=lambda: calculate()).grid(row=8, column=4, pady=1)
Button(root, text="f*ck", command=Exit2, width=6, height=2, bd=3).grid(row=8, column=5, pady=1)

root.mainloop()