# 创建一个四边形、平行四边形、矩形类，四边形为基类，平行四边形继承于四边形，矩形继承于平行四边形
# 在平行四边形中调用四边形的__init__，矩形调用平行四边形的__init__


class Quadrilateral:

    def __init__(self) -> None:
        print("我是四边形！")


class Parallelogram(Quadrilateral):
    def __init__(self) -> None:
        print("我是平行四边形！",1)
        super().__init__()


class Rectangle(Parallelogram):
    def __init__(self) -> None:
        print("我是矩形！",2)
        super().__init__()
        Quadrilateral.__init__(self)


rect = Rectangle()
