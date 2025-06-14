# 集合
# 集合是无序、唯一的元素集合，使用花括号 {} 或 set() 函数定义。

# 定义集合
m_set1 = {1, 2, 3, 4, 5}
m_set2 = set(m_set1)
empty_set = set()

print(m_set1)
print(m_set2)
print(empty_set)


# 添加元素
m_set1.add(6)
m_set2.update([4, 5, 6])
print(m_set1)
print(m_set2)

# 删除元素
m_set2.remove(6)
m_set2.discard(5)

print(m_set2)

# 数学运算
# 交集
print(m_set1 & m_set2)
# 并集
print(m_set1 | m_set2)
# 差集
print(m_set1 - m_set2)
