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



# con = sq.connect('saper.db')
with sq.connect('saper.db') as con:
    cur = con.cursor()  # cusor

    # cur.execute('DROP TABLE IF EXISTS users')  # delete table from DB IF EXISTS

    cur.execute('''CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,  
    name TEXT NOT NULL,
    sex INTEGER NOT NULL DEFAULT 1,
    old INTEGER,
    score INTEGER
    )''') # CREATE - creating table, PRIMARY KEY - main key - unicum for current table, NOT NULL - not null,
    # DEFAULT 1 - default value, AUTOINCREMENT - automatic increase value to 1 (but its also going automatically without this option)

    cur.execute('''INSERT INTO users (name, sex, old, score) VALUES 
    ('Serg', 1, 43, 1),
    ('Ser', 1, 43, 2),
    ('Sergey', 1, 43, 3),
    ('Sergio', 1, 43, 4),
    ('Sergiy', 1, 43, 5),
    ('Angel', 2, 38, 6),
    ('Angelina', 2, 38, 7),
    ('Ang', 2, 38, 8),
    ('Angelok', 2, 38, 9),
    ('Angelinka', 2, 38, 10),
    ('Mark', 1, 8, 3),
    ('Mar', 1, 8, 9),
    ('Mar4ik', 1, 8, 10),
    ('Marchik', 1, 8, 11),
    ('Mark', 1, 8, 8),
    ('Yarik', 1, 2, 23),
    ('Yar', 1, 2, 3),
    ('Yarosliv', 1, 2, 10),
    ('Yaroslavchik', 1, 2, 8)    
    ''')

# following comads execution automatically by context manager WITH
# co.commit()  -  save all change to DB
# con.close()  -  close DB
