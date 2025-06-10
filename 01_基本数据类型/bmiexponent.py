height = 1.70
weight = 75
bmi = weight / (height * height)
print("您的bmi指数为：" + str(bmi))
if bmi < 18.5:
    print("你的体重过轻")
if bmi >= 18.5 and bmi < 24.9:
    print("你的体重正常，继续保持")
if bmi > 24.9 and bmi < 29.9:
    print("你的体重过重，注意饮食习惯，多锻炼")
if bmi > 29.9:
    print("你已是肥胖，注意减肥")
