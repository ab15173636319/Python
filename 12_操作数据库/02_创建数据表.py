import pymysql

try:
    conn = pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        password="123456",
        database="data",
    )

    # 创建游标
    mycursor = conn.cursor()

    mycursor.execute(
        "create table if not exists goods(id int primary key auto_increment,name varchar(20),price float,count int,detail varchar(255))"
    )

    # 提交事务
    conn.commit()
    # 关闭游标
    mycursor.close()
    # 关闭连接
    conn.close()


except:
    print("发生错误")
