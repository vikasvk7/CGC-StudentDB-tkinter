from tkinter import *
import time
import sqlite3
import tkinter.messagebox as tmsg


db = sqlite3.connect("studentData.db")
db.execute("CREATE TABLE IF NOT EXISTS STUDENT(NAME CHAR[20], PHONE INT, BRANCH CHAR[20], PYTHON CHAR[5], JAVA CHAR[5], CPP CHAR[5])")


def check1():
    if (choice1.get()):
        ans = "yes"
    else:
        ans = "no"
    return ans

def check2():
    if (choice2.get()):
        ans = "yes"
    else:
        ans = "no"
    return ans

def check3():
    if (choice3.get()):
        ans = "yes"
    else:
        ans = "no"
    return ans


def action():
    flag = 0
    print("Submitting! Please wait",end = "")
    for i in range(5):
        print(".", end ="")
        time.sleep(0.3)

    crsr = db.execute("SELECT * FROM STUDENT")
    for row in crsr:
        if(row[0] == name1.get() and row[1] == phone1.get()):
            flag = 1
            tmsg.showerror("Database Error", "Data Already Present!")

    if(flag==0):
        db.execute("INSERT INTO STUDENT(NAME, PHONE, BRANCH, PYTHON, JAVA, CPP) VALUES(?,?,?,?,?,?)",(name1.get(), phone1.get(), branch1.get(), check1(), check2(), check3()));
        tmsg.showinfo("Success", "Done Successfully")
        db.commit()
    db.close()

def create():

    wid = Toplevel(root)

root = Tk()

root.geometry("445x420")

root.wm_iconbitmap("db.ico")


root.title("Student Database 2019")

cgc = PhotoImage(file = "cgc.png")
Label(root, image = cgc, padx = 10).grid(row = 0, column = 1, sticky = E)
Label(root, text = "Student Data", font = "tahoma 15 bold", pady = 15).grid(row = 1, column = 1)
Label(root, text = "Name: ", font="tahoma 10 bold", pady = 10).grid(row = 2, column=0,sticky = W)
Label(root, text = "Phone: ", font = "tahoma 10 bold",  pady = 10).grid(row=3,column = 0,sticky = W)
Label(root,text = "Branch: ", font = "tahoma 10 bold",  pady = 10).grid(row =4, column = 0,sticky = W)




name1 = StringVar()
phone1 = IntVar()
branch1 = StringVar()


name = Entry(root, textvariable = name1, width = 50).grid(row = 2,column = 1)
phone = Entry(root, textvariable = phone1, width = 50).grid(row = 3,column = 1)
branch = Entry(root, textvariable = branch1, width = 50).grid(row = 4,column = 1)

choice1 = IntVar()
choice2 = IntVar()
choice3 = IntVar()


Checkbutton(root, text = "Python",font = "tahoma 10 bold",pady = 15, variable = choice1,command = check1()).grid(row=5,column=0,sticky = W)
Checkbutton(root, text = "Java",font = "tahoma 10 bold", variable= choice2,command = check2()).grid(row=5,column=1)
Checkbutton(root, text = "C++",font = "tahoma 10 bold" ,variable = choice3,command = check3()).grid(row=5,column=2)

b = Button(root,text = "Submit", font = "tahoma 10 bold" ,command = action).grid(row = 6, column = 1)

Button(root, text = "View Data", command = create,font = "tahoma 10 bold", pady = 5).grid(column = 1)


root = mainloop()