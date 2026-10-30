import sqlite3

#连接数据库并建表
conn = sqlite3.connect("stus.db")
cursor = conn.cursor()
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS stus_info (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    gender TEXT NOT NULL
    )
    """
    )
cursor.close()
conn.commit()

#CRUD操作
#增
with sqlite3.connect("stus.db") as conn:
    cursor = conn.cursor()

    infos = [("Lin",20,"male"),("Li",21,"female"),("Wang",22,"male")]
    cursor.executemany("INSERT INTO stus_info (name, age, gender) VALUES (?, ?, ?)",infos)

#查询
with sqlite3.connect("stus.db") as conn:
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM stus_info")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

#改
with sqlite3.connect("stus.db") as conn:
    cursor = conn.cursor()

    cursor.execute("UPDATE stus_info SET age = ? WHERE name = ?",(15,'Li'))
    cursor.execute("SELECT * FROM stus_info")
    rows = cursor.fetchall()
    print("********修改后的数据↓**********")
    for row in rows:
        print(row)

#删除
with sqlite3.connect("stus.db") as conn:
    cursor = conn.cursor()

    cursor.execute("DELETE FROM stus_info")
    if(cursor.fetchall() == []):
        print("删除成功")