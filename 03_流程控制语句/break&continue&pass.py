# break
# 结束当前循环

# 如下列代码所示为一个死循环（一直运行下去的循环），
# 但运行结果却是有限的，因为当num1累加到10是就会进入判断内，break就会终止循环

# num1 = 1
# while 1 > 0:
#     print(num1)
#     num1 += 1
#     if num1 == 10:
#         break

# continue
# 跳过某次循环

# 如下列代码所示，当num2为6或7时，执行if条件下的代码片段，而continue作用就是跳过当前方法体内之后的代码运行

# num2 = 1
# while num2 <= 10:
#     if num2 == 6 or num2 == 7:
#         num2 += 1
#         continue
#     print(num2)
#     num2 += 1

# pass
# 表示不进行任何操作，通常占位使用
# 当语法上需要一个语句，但你暂时不需要执行任何代码时，可以使用 pass 来避免语法错误。

num3 = 1
while num3 <= 10:
    pass
