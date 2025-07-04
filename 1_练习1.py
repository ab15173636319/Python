# 定义一个字符串变量用于测试反转功能
str = "hello world"

# 方法1：使用切片[::-1]，从后向前步长为-1，直接反转字符串
print(str[::-1])

# 方法2：使用内置函数reversed()返回迭代器，再用join()组合成字符串
print(reversed(str))
print("".join(reversed(str)))

# 方法3：先将字符串转为列表，调用列表的reverse()方法反转，再组合成字符串
slist = list(str)
slist.reverse()
print("".join(slist))

