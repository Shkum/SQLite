import sqlite3 as sq

#
# Название	Описание
# NULL	Значение - значение NULL.
# INTEGER	Значение представляет собой целое число со знаком, сохраненное в 1, 2, 3, 4, 6 или 8 байтах в зависимости от величины значения.
# REAL	Значение представляет собой значение с плавающей запятой, которое хранится как 8-байтовое число с плавающей точкой IEEE.
# TEXT	Значение представляет собой текстовую строку, хранящуюся с использованием кодировки базы данных (UTF-8, UTF-16BE или UTF-16LE)
# BLOB	Значение представляет собой блок данных, который хранится точно так же, как он был введен.




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

# Template for searching - % - any continuation of the string
# Template for searching - _ - any next symbol

with sq.connect('saper.db') as con:
    cur = con.cursor()  # cusor

    #  set score for all users = 0
    # cur.execute('''
    # UPDATE users SET score = 0
    # ''')

    cur.execute('''
    UPDATE users SET score = 999 WHERE rowid = 1 OR sex = 2    
    ''')
    cur.execute('''
    UPDATE users SET score = score + 500 WHERE sex = 2   
    ''')

    cur.execute('''
    UPDATE users SET score = 999999000 WHERE name LIKE 'Sergei'    
    ''')

    cur.execute('''
    UPDATE users SET score = 11111111111111111 WHERE name LIKE 'Y%'    
    ''')

    cur.execute('''
    UPDATE users SET score = 55555555555555555 WHERE name LIKE 'Mar_'    
    ''')


    cur.execute('''
    UPDATE users SET score = 55555555555555555 WHERE name LIKE 'Mar_'    
    ''')


    cur.execute('''
    UPDATE users SET score = 1000000000000 WHERE name LIKE 'Ang_l%'    
    ''')

    cur.execute("UPDATE users SET score = 1, old = 43 WHERE old > 40")


############################################################################################

    cur.execute("DELETE FROM users WHERE rowid in (1, 40)")  # rowid will only increase and will not be deleted second time

    s = tuple(range(1, 40))
    cur.execute(f"DELETE FROM users WHERE rowid in {s}")
#
# con.close()
