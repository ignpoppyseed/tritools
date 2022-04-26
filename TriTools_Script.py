import tkinter as tk
import tkinter.messagebox
import webbrowser
menuitem = 0
window = tk.Tk()
window.resizable(width=False, height=False)
window.title("TriTools!")
window.geometry('400x200')
menufr = tk.Frame(master=window)
angle = tk.Frame(master=window)
credit = tk.Frame(master=window)

frame_l1 = tk.Frame(master = angle)
frame_l2 = tk.Frame(master = angle)
toplbl = tk.Label(angle, text = "Solve For Missing Angle")

lbl1 = tk.Label(frame_l1, text = "Angle 1: ")
lbl1.pack(side=tk.LEFT)

txt1 = tk.Entry(frame_l1, width=10)
txt1.pack(side=tk.LEFT)

lbl2 = tk.Label(frame_l2, text = "Angle 2: ")
lbl2.pack(side=tk.LEFT)

txt2 = tk.Entry(frame_l2, width=10)
txt2.pack(side=tk.LEFT)

def clicked():
    aa = txt1.get()
    ab = txt2.get()
    res = 180 - (float(aa) + float(ab))
    tkinter.messagebox.showinfo("Answer", f"Missing angle: {res}")

btn = tk.Button(angle, text = "Enter" ,
        fg = "black", command=clicked)

creditheader = tk.Label(credit, text = "Created by Poppy in Python3")
creditheader.pack(anchor='c')
creditdate = tk.Label(credit, text = "4/25/2022")
creditdate.pack(anchor='c')

def sitepage():
        webbrowser.open("https://cloverbrand.xyz")
def gitpage():
        webbrowser.open("https://github.com/ignpoppyseed/")


gitbtn = tk.Button(credit, text = "GitHub" ,
        fg = "black", command=gitpage)
gitbtn.pack(anchor='c')
sitbtn = tk.Button(credit, text = "Website" ,
        fg = "black", command=sitepage)
sitbtn.pack(anchor='c')

tri = tk.Frame(master=window)
frame_t1 = tk.Frame(master = tri)
frame_t2 = tk.Frame(master = tri)
frame_t3 = tk.Frame(master = tri)

toptrilbl = tk.Label(tri, text = "Check if Triangle is Valid")

trilbl1 = tk.Label(frame_t1, text = "Angle 1: ")
trilbl1.pack(side=tk.LEFT)

tritxt1 = tk.Entry(frame_t1, width=10)
tritxt1.pack(side=tk.LEFT)

trilbl2 = tk.Label(frame_t2, text = "Angle 2: ")
trilbl2.pack(side=tk.LEFT)

tritxt2 = tk.Entry(frame_t2, width=10)
tritxt2.pack(side=tk.LEFT)

trilbl3 = tk.Label(frame_t3, text = "Angle 2: ")
trilbl3.pack(side=tk.LEFT)

tritxt3 = tk.Entry(frame_t3, width=10)
tritxt3.pack(side=tk.LEFT)

def triclicked():
    ba = tritxt1.get()
    bb = tritxt2.get()
    bc = tritxt3.get()
    tri1 = (float(ba) + float(bb) + float(bc))
    if tri1 == 180:
        tkinter.messagebox.showinfo("Answer", f"Yes! That is a valid triangle!")
    else:
        tkinter.messagebox.showinfo("Answer", f"No. That is not a valid triangle.")

tribtn = tk.Button(tri, text = "Enter" ,
             fg = "black", command=triclicked)

def menudef1():
    tri.pack_forget()
    credit.pack_forget()
    global menuitem
    if menuitem == 1:
        pass
    else:
        credit.pack_forget()
        menuitem = 1

        toplbl.pack()
        frame_l1.pack()
        frame_l2.pack()
        btn.pack()
        angle.pack(fill=tk.BOTH, expand=True, anchor='s')
def menudef2():
    angle.pack_forget()
    credit.pack_forget()
    global menuitem
    if menuitem == 2:
        pass
    else:
        menuitem = 2
        toptrilbl.pack()
        frame_t1.pack()
        frame_t2.pack()
        frame_t3.pack()
        tribtn.pack()
        tri.pack(fill=tk.BOTH, expand=True, anchor='s')
def menudef3():
    tri.pack_forget()
    angle.pack_forget()
    global menuitem
    if menuitem == 3:
        pass
    else:
        menuitem = 3
        credit.pack(fill=tk.BOTH, expand=True, anchor='s')

menubtn1 = tk.Button(menufr, height = 2, text = "Find Missing Angle", fg = "black", command=menudef1)
menubtn1.pack(fill=tk.X, side=tk.LEFT, expand=True, anchor='n')
menubtn2 = tk.Button(menufr, height = 2, text = "Triangle Validator", fg = "black", command=menudef2)
menubtn2.pack(fill=tk.X, side=tk.LEFT, expand=True, anchor='n')
menubtn3 = tk.Button(menufr, height = 2, text = "View The Credits", fg = "black", command=menudef3)
menubtn3.pack(fill=tk.X, side=tk.LEFT, expand=True, anchor='n')
menufr.pack(fill=tk.X, expand=True, anchor='n')
window.iconbitmap('icon.ico')
window.mainloop()
