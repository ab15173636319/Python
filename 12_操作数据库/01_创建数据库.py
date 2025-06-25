import pymysql

try:
    conn = pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        password="123456",
    )

    # 创建游标
    mycursor = conn.cursor()
    # 执行创建数据库指令
    mycursor.execute("create database if not exists test_data")

    # 关闭游标
    mycursor.close()
    # 关闭连接
    conn.close()

except Exception as e:
    print(f"发生错误：{e}")
