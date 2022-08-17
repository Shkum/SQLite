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

# AGRIGATING FUNCTIONS:
# avg(X) - avg()возвращает среднее значение указанного поля
# count(*) - count(X)возвращает количество раз,которое X не NULL в группе
# count(X) - возвращает общее количество строк в группе -> подсчет числа записей
# group_concat(X)
# group_concat(X,Y) - возвращает строку,которая является конкатенцией всех не нулевых значений параметраX
# max(X) - нахождение максимального значения указанного поля
# min(X) - нахождение минимального значения указанного поля
# sum(X) - почсчет сумы указанного поля
# total(X) - возвращают сумму всех не-NULL значений в группе

# SELECT <fields> FROM <tables>
# JOIN <table1>, <table2>, etc
# ON <join conditions>

#  SELECT user_id, * FROM games, users ON users.name = games.nam
#  SELECT user_id, * FROM games, users


# __________________________

# SELECT name, sex, sum(games.score) as score
# FROM games
# JOIN users
# ON games.user_id = users.id
# GROUP BY user_id
# ORDER BY score DESC
# ____________________________

# UNION SELECT - join only unicum data

with sq.connect('saper.db') as con:
    cur = con.cursor()
    cur.execute('''
    SELECT score,`from` FROM tab1
    UNION SELECT val, type FROM tab2
    ''')
    s = cur.fetchall()
    for i in s:
        print(*i)

print('#'*50)

# unicum data only 100, 200, 300, 400
with sq.connect('saper.db') as con:
    cur = con.cursor()
    cur.execute('''
    SELECT score FROM tab1
    UNION SELECT val FROM tab2
    ''')
    s = cur.fetchall()
    for i in s:
        print(*i)



print('#'*50)

with sq.connect('saper.db') as con:
    cur = con.cursor()
    cur.execute('''
    SELECT score, 'from_table_1' as tbl FROM tab1
    UNION SELECT val, 'from_table_2' as tbl FROM tab2
    ''')
    s = cur.fetchall()
    for i in s:
        print(*i)


print('#'*50)

with sq.connect('saper.db') as con:
    cur = con.cursor()
    cur.execute('''
    SELECT score, 'from_table_1' as tbl FROM tab1
    UNION SELECT val, 'from_table_2' as tbl FROM tab2
    ORDER BY score DESC
    ''')
    s = cur.fetchall()
    for i in s:
        print(*i)
