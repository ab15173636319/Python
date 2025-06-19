# 与java语言，派生类可访问基类的属性和方法
# 实例化时，派生类不会访问基类的__init__方法
class Fruit:
    color = "红色"

    def __init__(self) -> None:
        print("我是一个水果")

    def harvest(self, color):
        print(f"水果是{color}的")
        print(f"水果已经收获")
        print(f"原来水果是{Fruit.color}的\n")


class Apple(Fruit):
    color = "红色"

    def __init__(self) -> None:
        print("我是一个苹果")

    # 方法重写，方法名相同，参数相同，返回值相同，方法体不同，调用时会调用子类的方法
    def harvest(self, color):
        print(f"苹果是{color}的")
        print(f"苹果已经收获")
        print(f"原来水果是{Fruit.color}的\n")


class peach(Fruit):
    color = "粉红色"

    def __init__(self) -> None:
        print("我是一个桃子")


apple = Apple()

apple.harvest(apple.color)

peach = peach()

peach.harvest(peach.color)
