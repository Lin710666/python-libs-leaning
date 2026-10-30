import os
import sqlite3

# 数据库文件固定放在 db.py 同级目录下，与「从哪个目录运行脚本」无关
DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "stus.db")

def init_db():
    # 连接数据库并建表
    with sqlite3.connect("学生信息管理系统项目/stus.db") as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS stus_info(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                stu_id TEXT NOT NULL,
                name TEXT NOT NULL,
                age INTEGER NOT NULL,
                gender TEXT NOT NULL,
                score INTEGER NOT NULL
            )
            """
        )
        conn.commit()
        cursor.close()

def add_stu(stu_id, name, age, gender, score):
    #添加学生信息
    with sqlite3.connect("学生信息管理系统项目/stus.db") as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO stus_info (stu_id, name, age, gender, score) VALUES (?, ?, ?, ?, ?)", (stu_id, name, age, gender, score))

def get_info(stu_id):
    #查询学生信息
    with sqlite3.connect("学生信息管理系统项目/stus.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM stus_info WHERE stu_id = ?", (stu_id,))
        return cursor.fetchall()

def  update_stu(stu_id, name=None, age=None, gender=None, score=None):
    #修改学生信息
    with sqlite3.connect("学生信息管理系统项目/stus.db") as conn:
        cursor = conn.cursor()
        if name:
            cursor.execute("UPDATE stus_info SET name = ? WHERE stu_id = ?", (name, stu_id))
        if age:
            cursor.execute("UPDATE stus_info SET age = ? WHERE stu_id = ?", (age, stu_id))
        if gender:
            cursor.execute("UPDATE stus_info SET gender = ? WHERE stu_id = ?", (gender, stu_id))
        if score:
            cursor.execute("UPDATE stus_info SET score = ? WHERE stu_id = ?", (score, stu_id))

def del_stu(stu_id):
    #删除学生信息
    with sqlite3.connect("学生信息管理系统项目/stus.db") as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM stus_info WHERE stu_id = ?", (stu_id,))

def view_whole():
    #查看所有学生信息
    with sqlite3.connect("学生信息管理系统项目/stus.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM stus_info")
        rows = cursor.fetchall()
        for row in rows:
            print(row)