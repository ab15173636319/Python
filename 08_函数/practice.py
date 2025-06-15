# 编写一个程序：实现输入人民币金额后，输出对应的美元、英镑、欧元和日元金额。1USD=7.18CNY,1GBP=9.76CNY,1EUR=8.31CNY,1JPY=0.05CNY


# def exchange_money(CNY):
#     USD = CNY / 7.18
#     GBP = CNY / 9.76
#     EUR = CNY / 8.31
#     JPY = CNY / 0.05
#     return f"可兑换{USD:.2f}美元、{GBP:.2f}英镑、{EUR:.2f}欧元、{JPY:.2f}日元"


# while True:
#     try:
#         CNY_money = float(input("请输入要兑换的金额（输入小于等于0的数字退出）："))
#         if CNY_money == -1 or CNY_money <= 0:
#             print("退出程序")
#             break
#         print(exchange_money(CNY_money))
#     except:
#         print("输入的金额有误，必须是数字！")


# 使用lambda对学生总成绩进行排序

students = [
    {
        "name": "张三",
        "student_id": "2025001",
        "scores": {"语文": 85, "数学": 92, "英语": 88, "物理": 76, "化学": 80},
        "total_score": 421,
        "average_score": 84.2,
    },
    {
        "name": "李四",
        "student_id": "2025002",
        "scores": {"语文": 90, "数学": 87, "英语": 93, "物理": 89, "化学": 91},
        "total_score": 450,
        "average_score": 89.2,
    },
    {
        "name": "王五",
        "student_id": "2025003",
        "scores": {"语文": 78, "数学": 85, "英语": 80, "物理": 92, "化学": 86},
        "total_score": 421,
        "average_score": 84.2,
    },
    {
        "name": "赵六",
        "student_id": "2025004",
        "scores": {"语文": 92, "数学": 76, "英语": 89, "物理": 83, "化学": 88},
        "total_score": 428,
        "average_score": 85.6,
    },
    {
        "name": "钱七",
        "student_id": "2025005",
        "scores": {"语文": 88, "数学": 94, "英语": 85, "物理": 87, "化学": 90},
        "total_score": 444,
        "average_score": 88.8,
    },
]


# 按总成绩排序
# sort列表对象自带的方法，其功能是对列表进行原地排序，也就是直接改变原列表的顺序，排序完成后不会返回新的列表。

students.sort(key=lambda x: x["total_score"], reverse=True)

print(students)
