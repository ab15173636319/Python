# 元组
# 元组是有序、不可变的序列，使用圆括号 () 定义。

# 定义元组

tuple1 = (1, 2, 3, 4)
tuple2 = (5, 6, 7, 8)

# 访问
print(tuple1[0])  # 1

# 解包
a, b, c, d = tuple1  # a=1,b=2,c=3,d=4

# 合并

tuple3 = tuple1 + tuple2

print(tuple3)
