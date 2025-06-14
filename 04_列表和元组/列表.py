# 列表
# 列表是有序、可变的序列，使用方括号 [] 定义，元素之间用逗号分隔。

# 创建列表
list = [1, 2, 3]
emputy_list = []

# 访问列表
print(list[0])
# 负数索引从后往前
print(list[-3])

# 修改元素

list[0] = -1
print(list)


# 添加元素

# 后加
list.append(4)  # [-1,2.3.4]

# 指定位置加入（第一位插入-2）
list.insert(0, -2)  # [-2,-1,2,3]
