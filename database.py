import sqlite3


db = sqlite3.connect("studentData.db")

cursor = db.execute("SELECT * FROM STUDENT")
db.execute("DELETE FROM STUDENT WHERE NAME = ?",("Sanskar",))
db.commit()
c = 0
db.commit()
for row in cursor :
    if(c==0):
        print("First Name  ", "Phone  ", "Branch  ", "Python  ", "Java  ", "C++  ")
        print("------------------------------------------------- ")
    print(row[0],"  ",row[1],"  ",row[2],"  ",row[3],"  ",row[4],"  ",row[5],"  " )
    c+=1



db.close()
