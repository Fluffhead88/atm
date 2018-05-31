
# Figure out what my database table looks like
# Design my menu workflow
# Develop my interaction with the database
# /// refactor database intercation to use an object

import records

db = records.Database("postgres://localhost/atm")

def make_transaction(db, amount):
    sql = "INSERT INTO bank (amount) VALUES (:amount);"
    return db.query(sql, amount=amount)

def make_balance(db, balance):
    sql = "INSERT INTO bank SUM(amount + balance) AS balance;"
    return db.query(sql, balance=balance)

def find_balance(db):
    sql = "SELECT balance FROM bank;"
    return db.query(sql)


def main_menu():
    print("1) Show Balance")
    print("2) Make a Withdrawl")
    print("3) Make a Deposit")
    print("4) Exit Program")
    choice = input("> ")
    return choice


def ui_find_balance(db):
    balances = find_balance(db)
    for balance in balances:
        print(f"Your balance is ${bank.balance}")
    print("Press <Enter> to go back to Main Menu")
    update_choice = input("> ")
    if update_choice == "":
        pass

def ui_make_withdraw(db):
    withdraw = input("How much would you like to withdraw? > ")
    withdraw = abs(int(withdraw)) * -1
    make_transaction(db, withdraw)
    make_balance(db, amount)
    print("Press <Enter> to go back to Main Menu")
    update_choice = input("> ")
    if update_choice == "":
        pass

def ui_make_deposit(db):
    deposit = input("How much would you like to deposit? > ")
    deposit = int(deposit)
    make_transaction(db, deposit)
    make_balance(db, amount)
    print("Press <Enter> to go back to Main Menu")
    update_choice = input("> ")
    if update_choice == "":
        pass

while True:
    my_choice = main_menu()
    if my_choice == "1":
        ui_find_balance(db)
    elif my_choice == "2":
        ui_make_withdraw(db)
    elif my_choice == "3":
        ui_make_deposit(db)
    elif my_choice == "4":
        exit()
