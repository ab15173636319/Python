# @property可将一个方法转为属性
# 调用时可不要()
# 作用于：计算属性、属性验证、访问控制。


class Rect:
    """我是一个矩形"""

    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height
        print(f"我是一个{width}cm * {height}cm的矩形")

    @property
    def area(self):
        return self.width * self.height


rect = Rect(10, 10)
print(rect.area)
