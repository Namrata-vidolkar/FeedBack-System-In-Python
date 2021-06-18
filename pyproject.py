import tkinter
from tkinter import messagebox
from tkinter import *
from tkinter import ttk

import sqlite3

con = sqlite3.connect("now.test")
print("connected")
sql = con.cursor()
q = "create table if not exists fd(a text,b text,c text,d text,e text)"
sql.execute(q);
con.commit()

main = Tk()
main.title("Feedback Form")
main.geometry("400x500+500+100")
label1 = Label(main, text="Feedback Form")
label1.place(x=140, y=10)
label1.config(font=5, fg="RED")

aa = StringVar()
bb = StringVar()
cc = StringVar()
dd = StringVar()
ee = StringVar()

q1 = Label(main, text="Q1:")
q2 = Label(main, text="Q2:")
q3 = Label(main, text="Q3:")
q4 = Label(main, text="Q4:")
q5 = Label(main, text="Q5:")

a = Entry(textvariable=aa, width=40)
b = Entry(textvariable=bb, width=40)
c = Entry(textvariable=cc, width=40)
d = Entry(textvariable=dd, width=40)
e = Entry(textvariable=ee, width=40)

q1.place(x=50, y=100)
q2.place(x=50, y=150)
q3.place(x=50, y=200)
q4.place(x=50, y=250)
q5.place(x=50, y=300)

a.place(x=100, y=100)
b.place(x=100, y=150)
c.place(x=100, y=200)
d.place(x=100, y=250)
e.place(x=100, y=300)


def showdata():
    show = Tk()
    show.title("Show Data")
    show.geometry("1200x310")
    label = Label(show, text="Display Data", font=15)
    label.place(x=580, y=10)
    tree = ttk.Treeview(show)
    tree["columns"] = ("Q1", "Q2", "Q3", "Q4", "Q5")
    tree.heading("Q1", text="Q1")
    tree.heading("Q2", text="Q2")
    tree.heading("Q3", text="Q3")
    tree.heading("Q4", text="Q4")
    tree.heading("Q5", text="Q5")

    q = "select * from fd";

    sql.execute(q)
    i = 1
    for row in sql.fetchall():
        tree.insert('', str(i), text='Form:' + str(i),
                    values=(str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4])))
        i = i + 1

    def del_data():
        q = "delete from fd";
        sql.execute(q)
        messagebox.showinfo("feedback", "all data is deleted")

    tbn = Button(show, text='del', command=del_data).place(x=0, y=280)
    tree.pack()
    tree.place(x=0, y=40)
    show.mainloop()


def adddata():
    q = "insert into fd values('" + aa.get() + "','" + bb.get() + "','" + cc.get() + "','" + dd.get() + "','" + ee.get() + "')"
    sql.execute(q)
    con.commit()
    messagebox.showinfo("Feedback", "Data Stored")


save = Button(main, text="<< Save >>", width=10, bg="black", fg="white", command=adddata)
show = Button(main, text="<< Display >>", width=10, bg="black", fg="white", command=showdata)

save.pack()
show.pack()

save.place(x=120, y=400)
show.place(x=220, y=400)

main.mainloop()