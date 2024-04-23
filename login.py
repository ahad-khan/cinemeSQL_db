import sqlite3

def login():
    running = True
    while running:
        username = str(input("Please enter your username: "))
        pin = str(input("Please enter your pin: "))
        with sqlite3.connect("cinema.db") as db:
            cursor = db.cursor()
            sql = ("select * from Employee where Username = ? and Pin = ?")
            cursor.execute(sql, [(username), (pin)])
            results = cursor.fetchall()

        if results:
            for i in results:
                print("Welcome", i[1])
                entry = True
                return entry
            break

        else:
            print("Username and password not recognised.")
            repeat = input("Would you like to try again?(y/n): ")
            if repeat.lower() == "n":
                print("Goodbye.")
                entry = False
                return entry