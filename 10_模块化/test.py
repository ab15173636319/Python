# 跳过import导入，但不建议使用，
# 仅当你知道导入的模块不在sys.path中，且你确定它在sys.path中不会改变时，才使用此方法。
# 此方法会改变Python解释器的行为，可能会导致一些不可预知的问题。
# 建议使用from ... import ...语句，明确导入需要的函数或变量。

import rect

print(rect.area(2, 3))
print(rect.perimeter(2, 3))


from circle import area, perimeter

print(area(4))
print(perimeter(4))
