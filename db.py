import sqlite3


conn = sqlite3.connect("database.db")
cursor = conn.cursor()

#Создание таблицы "Вещи"
def create_table_things():
    cursor.execute("""CREATE TABLE things
                      (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                       name TEXT, 
                       image TEXT,
                       owner TEXT)
                   """)

def create_table_wishes():
#Создание таблицы "Желания"
    cursor.execute("""CREATE TABLE wishes
                          (user TEXT,
                           id TEXT)
                       """)

#Внесение вещи в таблицу
def add_thing(name, image, owner):
    cursor.execute("""INSERT INTO things VALUES (NULL, ?, ?, ?)""", [(name), (image), (owner)])
    conn.commit()

#Внесение вещи в список желаний
def add_wish(user, id_wish):
    cursor.execute("""INSERT INTO wishes VALUES (NULL, ?, ?, ?)""", [(user), (id_wish)])
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


# create_table_things()
# add_thing('Самокат', 'http://.....', '@Ivan')
# add_thing('Велосипед', 'http://.....', '@Ivan')
# add_thing('Кепка', 'http://.....', '@username')
# print(get_thing(3))
# print(get_all_things('@Ivan'))
