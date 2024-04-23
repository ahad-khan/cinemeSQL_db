import sqlite3

# this file should
# obtain Username from Employee
# obtain EmployeeID where Username=username
# obtain CustomerID & Reserved from Reservation
# obtain LastName from

def select_transactions(id):
    with sqlite3.connect("cinema.db") as db:
        cursor = db.cursor()
        cursor.execute("""select Reservation.EmployeeID as employeeID,
                          Employee.Username as employee_username,
                          Reservation.CustomerID as customerID, 
                          Customer.Title as customer_t
                          Customer.FirstName as customer_fn,
                          Customer.LastName as customer_ln
                          Reserved, 
                          Paid, 
                          TotalPay, 
                          from Reservation
                          left join Employee on Reservation.employeeID = Employee.EmployeeID
                          left join Customer on Reservation.customerID = Customer.CustomerID
                          where Reservation.EmployeeID=?""", (id,))
        transaction = cursor.fetchall()
        print(transaction)

def get_id(username):
    with sqlite3.connect("cinema.db") as db:
        cursor = db.cursor()
        sql = ("select EmployeeID from Employee where Username = ?")
        cursor.execute(sql, [(username)])
        results = cursor.fetchone()
    select_transactions(results[0])

if __name__ == "__main__":
    user = str(input("Please re-enter your username: "))
    get_id(user)