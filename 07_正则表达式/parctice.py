import re


# 1.替换出现的违金词
string = """
    1. 违反国家法律，危害国家安全，构成犯罪，情节严重的，依法追究刑事责任；
    2. 其他违反国家法律的情况，由情节严重的，依法追究刑事责任。
"""

pattern = r"违反|犯罪|刑事|国家|法律"

result = re.sub(pattern, "***", string)

print(result)


# 2.提取文本中邮箱地址

content = """
    张三：13912345678@163.com
    李四：abc@163.com
    王五：123456@qq.com
    赵六：hello@126.com
    孙七：123456@163.com.cn
"""

pattern2 = r"\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b"

# [a-zA-Z0-9._%+-]+：允许用户名包含字母、数字、点、下划线、百分号、加减号，且不限制开头字符。
# [a-zA-Z0-9.-]+：匹配 @ 后的域名主体（如 163、gmail），允许字母、数字、点和连字符。
# [a-zA-Z]{2,}：正确匹配 .com、.cn、.net 等（至少两个字母）。
# \b：确保邮箱前后不是其他单词字符（如 hello@example.com 中的 lo@ex 不会被误匹配）。

result = re.findall(pattern2, content)

print(result)
