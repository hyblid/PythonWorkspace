import sqlite3

with sqlite3.connect("compayny.db") as db:
    cursor = db.cursor()
    
    cursor.execute("""CREATE TABLE IF NOT EXISTS EMPLOYEES (
        id integer PRIMARY KEY,
        name text NOT NULL,
        dept text NOT NULL,
        salary integer);""")
    
    cursor.execute("""INSERT INTO employees (id,name,dept,salary) 
                 VALUES("1", "bob", "Sales", "25000")""")
    db.commit()
    
    newID = input("Enter ID number: ")
    newName = input("Enter name: ")
    newDept = input("Enter department: ")
    newSalary = input("Enter salary: ")
    cursor.execute("""INSERT INTO employees (id,name, dept, salary) VALUES(?,?,?,?)""", 
                  (newID, newName, newDept,newSalary))
    db.commit()
    
    cursor.execute("SELECT * FROM employees")
    print(cursor.fetchall())
                 