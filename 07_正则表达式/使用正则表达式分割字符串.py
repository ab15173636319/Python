# split(正则表达式,字符串,最大拆分次数)

import re


string = "合抱之木，生于毫末；九层之台，起于累土；千里之行，始于足下。"

pattern = r"，"

result = re.split(pattern, string)

print(result)
