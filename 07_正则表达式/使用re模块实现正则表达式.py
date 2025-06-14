# 导入re模块
import re

# =================================================================

# 使用match()进行匹配
# match()是re的一个函数，用于：
# 从字符串开始位置尝试匹配正则表达式
# 如果匹配成功返回一个匹配对象
# 诺匹配失败返回none


# 匹配已字母开头且长度在[5,15]之间，再[5,15]位数字，以0结尾

pattern_str1 = "abcdefgHIJKLMN1234567890"

pattern1 = r"^[a-zA-Z]{5,15}\d{5,15}0$"

match1 = re.match(pattern1, pattern_str1)

print(match1)


# ==================================================================
# 使用search()进行匹配
# search()是re的一个函数，用于：
# 在整个字符串中任意位置开始匹配正则表达式，且只匹配一次
# 如果匹配成功返回一个匹配对象
# 若匹配失败返回none

# 匹配是否含有[abc]

pattern_str2 = "1234567890abcdefgHIJKLMN"

pattern2 = r"abc"

match2 = re.search(pattern2, pattern_str2)

print(match2)

# ==================================================================

# 使用findall()进行匹配
# findall()是re的一个函数，用于：
# 在整个字符串中任意位置开始匹配正则表达式，且匹配所有
# 如果匹配成功返回一个匹配对象列表(以列表的形式返回匹配的字符串)
# 若匹配失败返回空列表

pattern_str3 = "1234567890abcdefgHIJKLMN1234567890abcdefgHIJKLMN"

pattern3 = r"[a-zA-Z]{5,15}"

match3 = re.findall(pattern3, pattern_str3)

print(match3)
