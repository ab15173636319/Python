# 字典
# 字典是无序、键值对的集合，使用花括号 {} 定义，键和值用冒号 : 分隔，键必须唯一且不可变。

# 创建字典
my_dict = {"name": "Alice", "age": 25}
empty_dict = {}

# 访问元素
print(my_dict["name"])  # 输出：Alice
print(my_dict.get("city", "Unknown"))  # 输出：Unknown（不存在时返回默认值）

# 修改/添加元素
my_dict["age"] = 26  # 修改值
my_dict["city"] = "Beijing"  # 添加新键值对

# 删除元素
del my_dict["age"]  # 删除键值对
city = my_dict.pop("city")  # 删除并返回值

# 遍历字典
for key in my_dict:  # 遍历键
    print(key, my_dict[key])

for key, value in my_dict.items():  # 遍历键值对
    print(key, value)


# keys()返回所有键

# values()返回所有值
