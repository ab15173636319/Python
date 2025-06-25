# 连接数据库
# 安装pymysql库
# pip install pymysql

import pymysql

try:
    # 创建连接
    conn = pymysql.connect(
        host="localhost",  # 主机名（不包含端口）
        port=3306,  # 端口号单独设置
        user="root",
        password="123456",
        database="data",
        charset="utf8mb4",  # 使用更通用的utf8mb4字符集
        cursorclass=pymysql.cursors.DictCursor,  # 以字典形式返回结果
    )

    # 创建游标
    cursor = conn.cursor()

    # 查询数据
    sql = "SELECT * FROM user"
    cursor.execute(sql)
    print(cursor.fetchall())

    # 增加数据
    user = {"name": "张三", "gender": "男", "age": 18}
    insertSql = "insert into user(name,gender,age) values(%s,%s,%s)"
    cursor.execute(insertSql, (user["name"], user["gender"], user["age"]))
    conn.commit()  # 提交事务

    # 删除数据
    delSql = "delete from user where uid=%s"
    cursor.execute(delSql, 2)
    conn.commit()

    # 修改数据
    updateSql = "update user set name=%s,age=%s where uid=%s"
    cursor.execute(updateSql, ("小花", 20, 1))
    conn.commit()

    # 关闭连接
    conn.close()
except Exception as e:
    print(f"数据库连接失败：{e}")
