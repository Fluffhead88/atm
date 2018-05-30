
# connect to Database
# drop any tables if they exist
# create any tables I need
# insert any data I need

# do not create database from seed file

import records

db = records.Database("postgres://localhost/atm")

db.query("DROP TABLE IF EXISTS bank;")

create_query = """
CREATE TABLE bank (
    id SERIAL PRIMARY KEY,
    balance NUMERIC(15),
    amount NUMERIC(15)
);
"""

db.query(create_query)

insert_query = """
INSERT INTO bank (balance, amount) VALUES (100, 0);
"""
db.query(insert_query)
