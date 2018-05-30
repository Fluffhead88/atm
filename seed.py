
# connect to Database
# drop any tables if they exist
# create any tables I need
# insert any data I need

# do not create database from seed file

import records

db = records.Database("postgres://localhost/atm")

db.query("DROP TABLE IF EXISTS contacts;")

create_query = """
CREATE TABLE atm (
    id SERIAL PRIMARY KEY,
    balance VARCHAR(15),
    transaction VARCHAR(15),
    new_balance VARCHAR(15)
);
"""

db.query(create_query)

insert_query = """
INSERT INTO atm (balance, transaction, new_balance) VALUES ('1,000,000', '', '');
"""
db.query(insert_query)
