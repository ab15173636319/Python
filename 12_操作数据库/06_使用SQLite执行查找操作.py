import sqlite3

try:
    conn = sqlite3.connect("mrsorft.db")

    mycursor = conn.cursor()
    # 执行sql语句，查找所有用户
    mycursor.execute("select * from user")
    # 打印结果
    # fetchone()方法只返回一条数据
    # fetchall()方法返回所有数据
    # fetchmany(size)方法返回指定条数数据
    print(mycursor.fetchall())
    print(mycursor.fetchmany(1))
    mycursor.close()
    conn.close()
except Exception as e:
    print(f"数据库连接失败：{e}")
