from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *
import csv

class search:

    def sea(self):
        for o in self.t1.get_children():
            self.t1.delete(o)

        rd=open("buddhufile.csv","r")
        object=csv.reader(rd)
        for i in object:
            if self.txt3.get() in i[0]:
                self.t1.insert("",index=1,values=i)
        else:
            showinfo("my dictionary","sorry,could not find the word")

    def __init__(self):
        self.win=Tk()
        self.p1=PanedWindow(self.win)
        self.p2=PanedWindow(self.win)
        self.win.geometry("500x500")
        self.win.configure(bg="#337775")
        self.t1 = Treeview(self.p2,selectmode='browse', columns=("word", "meaning"))
        self.t1.column("word",width=250)
        self.t1.column("meaning",width=850)
        self.vsb=Scrollbar(self.win,orient='vertical',command=self.t1.yview)
        self.hsb=Scrollbar(self.win,orient='horizontal')
        self.hsb.configure(command=self.t1.xview)
        self.hsb.pack(side='bottom',fill='x')
        self.vsb.pack(side='right',fill='y')
        self.t1.configure(yscrollcommand=self.vsb.set)
        self.t1.configure(xscrollcommand=self.hsb.set)
        self.t1.heading("word", text="Word")
        self.t1.heading("meaning", text="Meaning")

        self.t1["show"] = "headings"
        rd = open("buddhufile.csv", 'r')
        object = csv.reader(rd)
        i = 0
        for l in object:
            self.t1.insert("", index=i, values=l)
            i += 1
        self.t1.pack(side='left')

        self.lb3=Label(self.p1,text="Enter Word")
        self.txt3=Entry(self.p1)
        self.bt2=Button(self.p1,text="Search",command=self.sea)
        self.lb3.grid(row=0,column=0)
        self.txt3.grid(row=0,column=1)
        self.bt2.grid(row=0,column=2)
        self.p1.pack()
        self.p2.pack()
        self.win.mainloop()

class demo():
    def test(self):
        wr=open("buddhufile.csv", "a",newline='')
        r=csv.writer(wr)
        p=[self.txt1.get(),self.txt2.get()]
        r.writerow(p)
        wr.close()
        showinfo("My Dictionary","Word Added")

    def ser(self):
        obj=search()

    def __init__(self):
        self.root=Tk()
        self.root.geometry("300x300")
        self.root.configure(bg="#337775")
        self.bt1=Button(self.root,text="submit",command=self.test)
        self.bt3=Button(self.root,text="Search Word",command=self.ser)
        self.lb1=Label(self.root,text="Enter Word")
        self.lb2=Label(self.root,text="Enter Meaning")
        self.txt1=Entry(self.root)
        self.txt2=Entry(self.root)

        self.lb1.grid(row=0,column=0)
        self.txt1.grid(row=0,column=1)
        self.lb2.grid(row=1,column=0)
        self.txt2.grid(row=1,column=1)
        self.bt1.grid(row=2,column=1)
        self.bt3.grid(row=3,column=1)
        self.root.mainloop()
#___________________________________________________



obj=demo()
