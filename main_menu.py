import sys, os

def menu():
    print("###### MAIN MENU #####")
    print()
    choice = int(input("""
                        (1) Create / Recreate Database
                        (2) Reinsert Database Records
                        (3) Update Database
                        (4) Insert a new entry
                        (5) Check all your transactions
                        (6) Quit
                         >   """))
    return choice