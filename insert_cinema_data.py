import sqlite3

def insert_data(values, table_name):
    with sqlite3.connect("cinema.db") as db:
        cursor = db.cursor()
        sql = "insert into Cinema (CinemaName, CinemaManager, CinemaAddress) values (?,?,?)"
        cursor.execute(sql, values)
        db.commit()

if __name__ == "__main__":
    n = int(input("How many enteries would you like to add to the table?: "))
    for i in range(n):
        a = str(input("What is the name of the cinema?: "))
        b = str(input("Who is the manager of the cinema?: "))
        c = str(input("Where is the cinema located?: "))
        final = (a, b, c)
        insert_data(final, "Cinema")
        print("Entry number ", i, "has been added!")