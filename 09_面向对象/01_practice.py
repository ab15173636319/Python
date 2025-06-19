# 创建一个汽车类


class Car:
    rank = "001"
    color = "红色"
    brand = "法拉利"
    mileage = "0Km"

    def __init__(self) -> None:
        print(
            f"这是一辆{self.brand}牌的车，颜色是{self.color}，型号是{self.rank}，里程数是{self.mileage}。"
        )

    def engine(self, mileage):
        self.mileage = mileage
        print(f"汽车启动，行驶了{self.mileage}公里。")


car = Car()
print(car.engine(600))
