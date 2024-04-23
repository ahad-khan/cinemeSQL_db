import sqlite3

def delete_data(data):
    with sqlite3.connect("cinema.db") as db:
        cursor = db.cursor()
        sql = "delete from Cinema where CinemaID=?"
        cursor.execute(sql, data)
        db.commit()

if __name__ == "__main__":
    data = str(input("What is the CinemaID of the Cinema you would like to delete?: "))
    delete_data(data)
    print("Entry has been successfully deleted!")