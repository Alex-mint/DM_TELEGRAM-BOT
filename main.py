import sqlite3


conn = sqlite3.connect("database.db")
cursor = conn.cursor()

#Создание таблицы
def create_table():
    cursor.execute("""CREATE TABLE things
                      (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                       name TEXT, 
                       image TEXT,
                       owner TEXT)
                   """)

#Внесение вещи в таблицу
def add_thing(name, image, owner):
    cursor.execute("""INSERT INTO things VALUES (NULL, ?, ?, ?)""", [(name), (image), (owner)])
    conn.commit()

#Получить вещь по id
def get_thing(id):
    sql = "SELECT * FROM things WHERE id = ?"
    cursor.execute(sql, [(id)])
    return cursor.fetchall()

#Получить все вещи одного хозяина
def get_all_things(owner):
    sql = "SELECT * FROM things WHERE owner = ?"
    cursor.execute(sql, [(owner)])
    return cursor.fetchall()


create_table()
add_thing('Самокат', 'http://.....', '@Ivan')
add_thing('Велосипед', 'http://.....', '@Ivan')
add_thing('Кепка', 'http://.....', '@username')
print(get_thing(3))
print(get_all_things('@Ivan'))
