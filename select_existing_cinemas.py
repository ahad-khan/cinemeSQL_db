import sqlite3

def select_all_cinemas():
    with sqlite3.connect("cinema.db") as db:
        cursor = db.cursor()
        cursor.execute("select * from Cinema")
        cinemas = cursor.fetchall()
        return cinemas

def select_single_cinema(id):
    with sqlite3.connect("cinema.db") as db:
        cursor = db.cursor()
        cursor.execute("select * from Cinema where CinemaID=?", (id,))
        cin = cursor.fetchone()
        return cin

def select_all_desc():
    with sqlite3.connect("cinema.db") as db:
        cursor = db.cursor()
        cursor.execute("select * from Cinema order by CinemaID DESC")
        cine = cursor.fetchall()
        return cine

if __name__ == "__main__":
    a = int(input("Would you like to:"
                  "\n(1) Display one single entry."
                  "\n(2) Display all entries."
                  "\n(3) Display descending by ID."
                  "\n> "))
    if a == 1:
        b = int(input("What is the CinemaID of the Cinema you wish to display?: "))
        cinemas = select_single_cinema(b)
        print(cinemas)
    elif a == 2:
        cinemas = select_all_cinemas()
        print(cinemas)
    elif a == 3:
        cinemas = select_all_desc()
        print(cinemas)
    else:
        print("An error has occurred!")
