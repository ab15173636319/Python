import copy

# 原始列表（包含不可变元素和嵌套字典）
original = [1, 2, 3, 4, 5, {"name": "小花", "age": 18}]

# 1. 直接赋值（共享引用）
assigned = original

# 2. 浅拷贝（仅复制第一层，嵌套对象共享引用）
shallow_copied1 = original[:]  # 切片操作
shallow_copied2 = list(original)  # 工厂函数
shallow_copied3 = copy.copy(original)  # copy模块的浅拷贝函数

# 3. 深拷贝（完全独立的副本）
deep_copied = copy.deepcopy(original)

# 修改原始列表的不可变元素
original[0] = 100
print("修改不可变元素后:")
print(f"原始列表: {original}")
print(f"直接赋值: {assigned}")
print(f"浅拷贝1: {shallow_copied1}")
print(f"深拷贝: {deep_copied}")
print("\n")

# 修改原始列表的嵌套字典
original[5]["age"] = 20
print("修改嵌套字典后:")
print(f"原始列表: {original}")
print(f"直接赋值: {assigned}")
print(f"浅拷贝1: {shallow_copied1}")
print(f"深拷贝: {deep_copied}")
