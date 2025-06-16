class Person:
    """人类"""  # 添加说明

    # 类属性
    weight = "70kg"
    height = "170cm"

    # 私有化属性

    __girlFirend = "小红"

    # 构造函数，对象被创建时自动调用
    # self参数是必须的，指向类本身的属性和方法
    def __init__(self, name, age, gender) -> None:
        print("我是：", name)
        print(f"我今年：{age}岁")
        print(f"我是：{gender}生")
        # 访问类属性
        print(f"我的体重是：{self.weight}")
        print(f"我的身高是：{self.height}")

    # 创建实例方法
    def run(sef, far):
        print(f"我跑了{far}km")

    # 私有化方法
    def __changeGirlFriend(self, girlFriend):
        self.__girlFirend = girlFriend


# 实例化对象
person = Person("张三", 18, "男")

# 修改类属性
Person.weight = "80kg"
# 访问类属性
print(Person.weight)

person.run(10)


# 访问私有化属性：实例化对象名_类名__属性名
print(f"女朋友是：{person._Person__girlFirend}")

# 调用私有化方法
person._Person__changeGirlFriend("小芳")
print(f"女朋友是：{person._Person__girlFirend}")
