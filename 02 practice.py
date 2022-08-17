import sqlite3 as sq

# INSERT INTO users (5, 'Ser', 1, 43, 1) # - insert new record
# INSERT INTO users (name, old, score) VALUES ('Ser', 43, 1) # - insert new record

# SELECT name, old, score, FROM users  # - reading values from database
# SELECT * FROM users  # - reading all values from database table
# SELECT * FROM users WHERE score > 2  # - reading values from database table if score > 2
# SELECT * FROM users WHERE score BETWEEN 2 AND 4  # - reading values from database table if score between 2 and 4
# SELECT * FROM users WHERE score == 3  # - reading values from database table if score == 3
# SELECT name, old, score FROM users WHERE old > 8 AND score > 1  #  reading from DB with several conditions

# conditions: AND, OR, NOT, IN NOT IN

# ORDER BY old # - sort by followed column
# ORDER BY old DESC # - sort by followed column - decreasing
# ORDER BY old ASC # - sort by followed column - increasing

# LIMIT 2  #  - how many records to read maximum
# LIMIT 2 [OFFSET 2] #  - how many records to read maximum, but bypass first offset values
# LIMIT <offset, max> #  - same as above

# SELECT * FROM users WHERE score > 2 ORDER BY score DESC LIMIT 5 OFFSET 2 # - EXAMPLE !!!!!!!!!!!!!!
# SELECT * FROM users WHERE score > 2 ORDER BY score DESC LIMIT 2, 5 # - SAME EXAMPLE !!!!!!!!!!!!!!


# UPDATE - update row in the tables

# DELETE - delete row from the table

with sq.connect('saper.db') as con:
    cur = con.cursor()  # cusor

    cur.execute("SELECT * FROM users WHERE score > 1 ORDER BY score DESC LIMIT 5")
    result = cur.fetchall()  # read all values
    print(result)
    print()
    for i in result:
        print(i)

    print()
    cur.execute("SELECT * FROM users WHERE score > 1 ORDER BY score DESC LIMIT 5")
    result1 = cur.fetchone() # read one value
    print(result1)

    print()
    cur.execute("SELECT * FROM users WHERE score > 1 ORDER BY score DESC LIMIT 5")
    result2 = cur.fetchmany(2) # read X values
    print(result2)

# following comads execution automatically by context manager WITH
# co.commit()  -  save all change to DB
# con.close()  -  close DB
