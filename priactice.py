import sqlite3

with sqlite3.connect("movie.db") as db:
    cursor = db.cursor()
    
    cursor.execute("""CREATE TABLE IF NOT EXISTS MOVIES (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title text NOT NULL,
        year text NOT NULL,
        stars text NOT NULL);""")
    
    cursor.execute("""INSERT INTO movies (title, year, stars) 
                 VALUES("terminaotr", "1955", "4")""")
    db.commit()
    
    title = input("Enter TITLE: ")
    year = input("Enter YEAR: ")
    stars = input("Enter STARS  : ")
    cursor.execute("""INSERT INTO movies (title, year, stars) VALUES(?,?,?)""", 
                  (title, year, stars))
    
    db.commit()
    
    cursor.execute("SELECT * FROM MOVIES")
    print(cursor.fetchall())
                 