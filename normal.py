
# Figure out what my database table looks like
# Design my menu workflow
# Develop my interaction with the database
# /// refactor database intercation to use an object

import records

db = records.Database("postgres://localhost/atm")

def find_balance(db, balance):
    sql = "SELECT * FROM atm WHERE balance = :balance;"
    return db.query(sql, balance=balance)
