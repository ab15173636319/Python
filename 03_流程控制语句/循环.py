# while循环
# 条件满足时循环执行

# 今有一个数，三三数余2，五五数余三，七七数余二，问几何？
# num = 1
# while num <= 10000:
#     if num % 3 == 2 and num % 5 == 3 and num % 7 == 2:
#         print(num)
#     num += 1


# for循环
# 一般在指定长度内循环

# 计算公差为1，首项为1的等差数列前100之和

sum = 1
for n in range(2, 101):
    sum += n
print(sum)

# 遍历字符串

for char in "我不吃牛肉！":
    print(f"{char}\n")
