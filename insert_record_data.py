import sqlite3
import pandas as pd
from pandas import ExcelWriter, ExcelFile

def query(sql, data):
    with sqlite3.connect("cinema.db") as db:
        cursor = db.cursor()
        cursor.execute("PRAGMA foreign_keys = ON")
        cursor.execute(sql, data)
        db.commit()

def insert_cinema_data(records):
    sql = "insert into Cinema (CinemaName, CinemaManager, CinemaAddress, CinemaPhone) values (?,?,?,?)"
    for record in records:
        query(sql, record)

def get_cinema_data():
    CinemaName = []
    CinemaManager = []
    CinemaAddress = []
    CinemaPhone = []
    df = pd.read_excel('Cinema.xlsx', sheet_name='Cinema')
    for i in df.index:
        CinemaName.append((df['CinemaName'][i]))
        CinemaManager.append((df['CinemaManager'][i]))
        CinemaAddress.append((df['CinemaAddress'][i]))
        CinemaPhone.append((df['CinemaPhone'][i]))
        x = [(CinemaName[i], CinemaManager[i], CinemaAddress[i], CinemaPhone[i])]
        insert_cinema_data(x)

def insert_screen_data(records):
    sql = "insert into Screen (SeatNum, RowNum) values (?,?)"
    for record in records:
        query(sql, record)

def get_screen_data():
    SeatNum = []
    RowNum = []
    df = pd.read_excel('Cinema.xlsx', sheet_name='Screen')
    for i in df.index:
        SeatNum.append(int((df['SeatNum'][i])))
        RowNum.append(int((df['RowNum'][i])))
        x = [(SeatNum[i], RowNum[i])]
        insert_screen_data(x)

def insert_movie_data(records):
    sql = "insert into Movie (MovieName, MovieDirector, MovieDuration, MovieRating) values (?,?,?,?)"
    for record in records:
        query(sql, record)

def get_movie_data():
    MovieName = []
    MovieDirector = []
    MovieDuration = []
    MovieRating = []
    df = pd.read_excel('Cinema.xlsx', sheet_name='Movie')
    for i in df.index:
        MovieName.append((df['MovieName'][i]))
        MovieDirector.append((df['MovieDirector'][i]))
        MovieDuration.append((df['MovieDuration'][i]))
        MovieRating.append(float((df['MovieRating'][i])))
        x = [(MovieName[i], MovieDirector[i], MovieDuration[i], MovieRating[i])]
        insert_movie_data(x)


def insert_movie_showing_data(records):
    sql = "insert into MovieShowings (CinemaID, MovieID, ScreenID, ShowStart, ShowEnd, Price) values (?,?,?,?,?,?)"
    for record in records:
        query(sql, record)

def get_movie_showing_data():
    CinemaID = []
    MovieID = []
    ScreenID = []
    ShowStart = []
    ShowEnd = []
    Price = []

    df = pd.read_excel('Cinema.xlsx', sheet_name='MovieShowing')
    for i in df.index:
        CinemaID.append(int((df['CinemaID'][i])))
        MovieID.append(int((df['MovieID'][i])))
        ScreenID.append(int((df['ScreenID'][i])))
        ShowStart.append(str((df['ShowStart'][i])))
        ShowEnd.append(str((df['ShowEnd'][i])))
        Price.append(float((df['Price'][i])))
        x = [(CinemaID[i], MovieID[i], ScreenID[i], ShowStart[i], ShowEnd[i], Price[i])]
        insert_movie_showing_data(x)


def insert_employee_data(records):
    sql = "insert into Employee (Username, Pin, SalaryCheck) values (?,?,?)"
    for record in records:
        query(sql, record)

def get_employee_data():
    Username = []
    Pin = []
    SalaryCheck = []

    df = pd.read_excel('Cinema.xlsx', sheet_name='Employee')
    for i in df.index:
        Username.append(str((df['Username'][i])))
        Pin.append(str((df['Pin'][i])))
        SalaryCheck.append(bool((df['SalaryCheck'][i])))
        x = [(Username[i], Pin[i], SalaryCheck[i])]
        insert_employee_data(x)


def insert_customer_data(records):
    sql = "insert into Customer (FirstName, LastName, Title) values (?,?,?)"
    for record in records:
        query(sql, record)

def get_customer_data():
    FirstName = []
    LastName = []
    Title = []
    df = pd.read_excel('Cinema.xlsx', sheet_name='Customer')
    for i in df.index:
        FirstName.append(str((df['FirstName'][i])))
        LastName.append(str((df['LastName'][i])))
        Title.append(str((df['Title'][i])))
        x = [(FirstName[i], LastName[i], Title[i])]
        insert_customer_data(x)

def insert_reservation_data(records):
    sql = "insert into Reservation (ScreenID, EmployeeID, CustomerID, ContactNum, ContactName, Reserved, Paid, TotalPay) values (?,?,?,?,?,?,?,?)"
    for record in records:
        query(sql, record)

def get_reservation_data():
    ScreenID = []
    EmployeeID = []
    CustomerID = []
    ContactNum = []
    ContactName = []
    Reserved = []
    Paid = []
    TotalPay = []
    df = pd.read_excel('Cinema.xlsx', sheet_name='Reservation')
    for i in df.index:
        ScreenID.append(int((df['ScreenID'][i])))
        EmployeeID.append(int((df['EmployeeID'][i])))
        CustomerID.append(int((df['CustomerID'][i])))
        ContactNum.append(str((df['ContactNum'][i])))
        ContactName.append(str((df['ContactName'][i])))
        Reserved.append(bool((df['Reserved'][i])))
        Paid.append(bool((df['Paid'][i])))
        TotalPay.append(float((df['TotalPay'][i])))
        x = [(ScreenID[i], EmployeeID[i], CustomerID[i], ContactNum[i], ContactName[i], Reserved[i], Paid[i], TotalPay[i])]
        insert_reservation_data(x)


if __name__ == "__main__":
    get_cinema_data()
    print("Cinema data has been inserted")
    get_screen_data()
    print("Screen data has been inserted")
    get_movie_data()
    print("Movie data has been inserted")
    get_movie_showing_data()
    print("MovieShowing data has been inserted")
    get_employee_data()
    print("Employee data has been inserted")
    get_customer_data()
    print("Customer data has been inserted")
    get_reservation_data()
    print("Reservation data has been inserted")
    print("All data inserted successfully")
