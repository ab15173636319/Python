# 格式化占位符 %s

# 将字符串 "4" 插入到占位符 %s 的位置
str = "123%s567" % "4"
print(str)


# 使用占位符{}

str2 = "我今天吃的是{}"
print(str2.format("苹果"))

# 多个占位符
str3 = "我今天吃的是{}，我今天喝的是{}"
print(str3.format("苹果", "葡萄汁"))

# 也可使用索引
str4 = "我今天吃的是{0}，我今天喝的是{1}，但{0}好像有点变质了。"
print(str4.format("苹果", "葡萄汁"))

# 也可使用关键字
str5 = "我今天吃的是{food}，我今天喝的是{drink}，但{food}好像有点变质了。"
print(str5.format(food="苹果", drink="葡萄汁"))

