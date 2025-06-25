import sqlite3

# 连接到SQLite数据库
# 连接mrsorft.db，诺不存在则创建
conn = sqlite3.connect("mrsorft.db")

# 创建游标
mycursor = conn.cursor()

# 执行sql语句，创建一个user表

# INTEGER PRIMARY KEY为SQLite的自动增长主键
mycursor.execute(
    "create table if not exists user (uid INTEGER PRIMARY KEY,name varchar(20),age int)"
)

mycursor.close()
conn.close()
