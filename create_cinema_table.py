import sqlite3

def create_table(db_name, table_name, sql):

    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        cursor.execute("select name from sqlite_master where name = ?", (table_name,))  # checks if the Cinema table has been created before
        result = cursor.fetchall()
        table_check = True
        if len(result) == 1:
            output = input("The table %s already exists, do you wish to recreate it (y/n): " %(table_name)).lower()
            if output == "y":
                table_check = False
                print("The table will be recreated - all data will be terminated")
                cursor.execute("drop table if exists {0}".format(table_name))
                db.commit()
            else:
                print("The existing table will be kept.")
        else:
            table_check = False
        if not table_check:
            cursor.execute(sql)
            db.commit()

def create_cinema_table():
    sql = """create table Cinema
            (CinemaID integer,
            CinemaName text,
            CinemaManager text,
            CinemaAddress text,
            CinemaPhone text,
            primary key(CinemaID))"""
    create_table(db_name, "Cinema", sql)

def create_screens_table():
    sql = """create table Screen
            (ScreenID integer,
            SeatNum int,
            RowNum int,
            primary key(ScreenID))"""
    create_table(db_name, "Screen", sql)

def create_movies_table():
    sql = """create table Movie
            (MovieID integer,
            MovieName text,
            MovieDirector text,
            MovieDuration int,
            MovieRating float,
            primary key(MovieID))"""
    create_table(db_name, "Movie", sql)

def create_movie_showings_table():
    sql = """create table MovieShowings
            (MovieShowingID integer,
            CinemaID integer,
            MovieID integer,
            ScreenID integer,
            ShowStart text,
            ShowEnd text,
            Price float,
            primary key(MovieShowingID),
            foreign key(CinemaID) references Cinema(CinemaID),
            foreign key(MovieID) references Movie(MovieID),
            foreign key(ScreenID) references Screen(ScreenID))"""
    create_table(db_name, "MovieShowing", sql)

def create_employee_table():
    sql = """create table Employee
            (EmployeeID integer,
            Username text,
            Pin text,
            SalaryCheck bool,
            primary key(EmployeeID))"""
    create_table(db_name, "Employee", sql)

def create_customer_table():
    sql = """create table Customer
            (CustomerID integer,
            FirstName text,
            LastName text,
            Title text,
            primary key(CustomerID))"""
    create_table(db_name, "Customer", sql)

def create_reservation_table():
    sql = """create table Reservation
            (ReservationID integer,
            ScreenID integer,
            EmployeeID integer,
            CustomerID integer,
            ContactNum text,
            ContactName text,
            Reserved bool,
            Paid bool,
            TotalPay float,
            primary key(ReservationID),
            foreign key(ScreenID) references Screen(ScreenID),
            foreign key(EmployeeID) references Employee(EmployeeID),
            foreign key(CustomerID) references Customer(CustomerID))"""
    create_table(db_name, "Reservation", sql)


