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


# LIKE - condition ( same as if XXX = YYY) (Функция like ()
# используется для реализации выражения «Y LIKE X [ESCAPE Z]»)

# Следующий оператор SQLite вернет те строки из таблицы author, в которых имя автора начинается с символа «W».
# # SELECT aut_name, country
# FROM author
# WHERE LIKE('W%',aut_name)=1;


# in the brackets () we may use nested query


cars = [
    ('Audi', 52642),
    ('Mercedes', 57127),
    ('Skoda', 9000),
    ('Volvo', 29000),
    ('Bentley', 350000),
]




#with sq.connect('saper.db') as con:

# all changse after BEGIN will be rollbacked in case of error during operations with BD after BEGIN
con = None

try:
    con = sq.connect('saper.db')
    cur = con.cursor()
    cur.executescript(''' CREATE TABLE IF NOT EXISTS cars 
    (
    car_id INTEGER PRIMARY KEY AUTOINCREMENT,
    model TEXT,
    price INTEGER
    );
    BEGIN;
    INSERT INTO cars VALUES (NULL, 'Audi', 52642);
    INSERT INTO cars VALUES (NULL, 'Mercedes', 57127);
    INSERT INTO cars VALUES (NULL, 'Skoda', 9000);
    INSERT INTO cars VALUES (NULL, 'Volvo', 29000);
    INSERT INTO cars VALUES (NULL, 'Bentley', 350000);
    UPDATE cars SET price = price + 1000000
    ''')


    # 1 Option:
    # cur.execute("INSERT INTO cars VALUES (1, 'Audi', 52642)")
    # cur.execute("INSERT INTO cars VALUES (2, 'Mercedes', 57127)")
    # cur.execute("INSERT INTO cars VALUES (3, 'Skoda', 9000)")
    # cur.execute("INSERT INTO cars VALUES (4, 'Volvo', 29000)")
    # cur.execute("INSERT INTO cars VALUES (5, 'Bentley', 350000)")


    # 2 Option:
    # for car in cars:
    #     cur.execute("INSERT INTO cars VALUES(NULL, ?, ?)", car)


    # 3 Option:
    # cur.executemany("INSERT INTO cars VALUES(NULL, ?, ?)", cars)

    ### cur.execute("UPDATE cars SET price = :Price WHERE model LIKE 'A%'", {'Price':0})

    # insert 'Price' to price = : Price, so it will be price = 0 for all models starting wiht letter 'A'
    # ? - unnamed parameters
    # price = :Price - named parameters


    # to exequte several comands use executescript and dot with koma to separate comands
    # delete all models starting with A
    # for all remaining cars increase prise for 1000
    # add Audi to table

    ### cur.executescript("""
    ### DELETE FROM cars WHERE model LIKE 'A%';
    ### UPDATE cars set price = price + 1000;
    ### INSERT into cars VALUES(NULL, 'Audi', 55000)
    ### """)

    con.commit()

except sq.Error as e:
    if con:
        con.rollback()
        print("Query handling error")
finally:
    if con:
        con.close()



    # following commands execution automatically by context manager WITH
    # co.commit()  -  save all change to DB
    # con.close()  -  close DB
