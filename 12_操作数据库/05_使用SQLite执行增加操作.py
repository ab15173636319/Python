import sqlite3

try:
    conn = sqlite3.connect("mrsorft.db")

    mycursor = conn.cursor()
    mycursor.execute("insert into user(name,age) values(?,?)", ("李四", 18))
    conn.commit()
    mycursor.close()
    conn.close()


except Exception as e:
    print(f"数据库连接失败：{e}")
