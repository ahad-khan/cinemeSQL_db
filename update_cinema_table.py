import sqlite3

def update_data(data):
    with sqlite3.connect("cinema.db") as db:
        cursor = db.cursor()
        sql = "update Cinema set CinemaName=?, CinemaManager=?, CinemaAddress=? where CinemaID=?"
        cursor.execute(sql, data)
        db.commit()

if __name__ == "__main__":
    a = int(input("What CinemaID would you like to update?: "))
    b = str(input("New name of the cinema?: "))
    c = str(input("New manager of the cinema?: "))
    d = str(input("New cinema location?: "))
    data = (b, c, d, a)
    update_data(data)
    print("Data successfully updated!")