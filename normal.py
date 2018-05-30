
# Figure out what my database table looks like
# Design my menu workflow
# Develop my interaction with the database
# /// refactor database intercation to use an object

import records

db = records.Database("postgres://localhost/atm")

def find_balance(db):
    sql = "SELECT balance FROM bank;"
    return db.query(sql)

def make_transaction(db, amount):
    sql = "INSERT INTO bank (amount) VALUES (:amount);"
    return db.query(sql, amount=amount)

def make_withdrawl(db):
    amount = input("How much would you like to withdraw? > ")
    amount = abs(int(amount)) * -1
    make_transaction(db, amount)
    return amount

def make_deposit(db):
    amount = input("How much would you like to deposit? > ")
    amount = int(amount)
    make_transaction(db, amount)
    return amount



def display_balance(bank):
    print(f"Your balance is ${bank.balance}")

def display_deposit(bank):
    print(f"You deposited ${bank} into your account.")

def display_withdrawl(bank):
    print(f"You withdrew ${bank} out of your account.")


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
        display_balance(balance)
    print("Press <Enter> to go back to Main Menu")
    update_choice = input("> ")
    if update_choice == "":
        pass

def ui_make_withdrawl(db):
    withdrawl = make_withdrawl(db)
    display_withdrawl(withdrawl)
    print("Press <Enter> to go back to Main Menu")
    update_choice = input("> ")
    if update_choice == "":
        pass

def ui_make_deposit(db):
    deposit = make_deposit(db)
    display_deposit(deposit)
    print("Press <Enter> to go back to Main Menu")
    update_choice = input("> ")
    if update_choice == "":
        pass

while True:
    my_choice = main_menu()

    if my_choice == "1":
        ui_find_balance(db)
    elif my_choice == "2":
        ui_make_withdrawl(db)
    elif my_choice == "3":
        ui_make_deposit(db)
    elif my_choice == "4":
        exit()
