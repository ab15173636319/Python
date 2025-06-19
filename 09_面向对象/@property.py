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
# print(rect.area)


# 创建的类属性或实例可能会被外部1修改，为了保护数据安全，我们会将这些属性或方法私有化，然而私有化的属性或方法
# 只能在类的内部被访问，外部无法直接访问。
# 为了方便外部访问，我们可以使用@property


class TV_show:
    __TV_name = "《变形金刚》"

    def __init__(self, tv_name) -> None:
        self.__TV_name = tv_name

    @property
    def show(self):
        return f"正在播放{self.__TV_name}"


tv = TV_show("《我是机器人》")

print(tv.show)