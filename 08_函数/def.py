# 创建函数
def sum_1_2():
    return 1 + 2


# 调用函数（带参数）
print(sum_1_2())  # 输出: 3


def add_numbers(a, b):
    return a + b


# 调用函数
print(add_numbers(1, 2))  # 输出: 3


# 第三个函数：计算任意数量位置参数的和
# 任意参数说明：*args 接受任意多个位置参数，并将其放在一个元组中，如：sum_numbers(1, 2, 3, 4)
# 任意参数说明：**kwargs 接受任意多个关键字参数，并将其放在一个字典中，如：sum_numbers(a=1, b=2, c=3)


def sum_numbers(*args):
    total = 0
    for num in args:
        print(f"加{num}")
        total += num
    return total


print(sum_numbers(1, 22, 33, 4))


# 返回类型->int
def sum_numbers(a: int, b: int) -> int:
    return a + b


# 调用函数
print(sum_numbers(1, 2))  # 输出: 3
