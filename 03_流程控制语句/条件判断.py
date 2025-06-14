# 1,
# if...else判断

# num = float(input("请输入半径r或边长a："))
# if num < 10 and num >= 0:
#     print(f"圆的面积为：{num*3.14**2}")
# else:
#     print(f"正方形面积为：{num**2}")


# 2，
# if...elif...else

# num = float(input("请输入半径r或边长a："))
# if num < 10 and num >= 0:
#     print(f"圆的面积为：{num*3.14**2}")
# elif num >= 10 and num < 100:
#     print(f"正方形面积为：{num**2}")
# else:
#     print(f"输入的值超出范围！")

# 3，
# match...case语句：相当于java的switch...case

# 匹配字面值
# from datetime import datetime

# day = datetime.today().weekday()
# match day:
#     case 0:
#         print("今天是星期1！")
#     case 5 | 6:
#         print("今天是周末！")
#     case _:
#         print("今天是工作日！")

# 绑定变量
# 诺在case中绑定一个并不存在的变量，则会将该变量与条件匹配，类似声明变量并赋值

# point = eval(input("请输入一个坐标"))
# match point:
#     case (0, 0):
#         print(f"{point}是原点")
#     case (0, y):
#         print(f"该点在y轴上，且y轴坐标为{y}")
#     case (x, 0):
#         print(f"该点在x轴上，且y轴坐标为{x}")
#     case (x, y):
#         print(f"该点x轴坐标为{x}，y轴坐标为{y}")

# 约束项
# 使用if语句
point = eval(input("请输入一个坐标"))
match point:
    case (x, y) if x > 0 and y > 0:
        print("该点在第一象限")
    case (x, y) if x > 0 and y < 0:
        print("该点在第四象限")
    case (x, y) if x < 0 and y < 0:
        print("该点在第三象限")
    case (x, y) if x < 0 and y > 0:
        print("该点在第二象限")
    case (0, 0):
        print("该点为原点")
    case (0, y):
        print(f"该点在y轴上，且y轴坐标为{y}")
    case (x, 0):
        print(f"该点在x轴上，且y轴坐标为{x}")
