# 判断用户名是否重复，不区分大小写

# exmple = ["bilL", "tOm", "PeTeR"]
# input_val = input("请输入用户名：")
# for item in exmple:
#     if input_val.upper() == item.upper():
#         print("重复！")
#         break
#     else:
#         exmple.append(input_val)
# print(exmple)


# 格式化输出商品和标号和单价：首先输入一些销售数据（包括商品号、商品名、单价），
#                          然后输出商品信息中商品号用6位数输出，
#                          单价保留2位小数，前面加￥符号

products = []

while True:
    # 获取用户输入的商品ID
    good_id = input("请输入商品号(输入0退出): ")
    
    # 检查是否退出
    if good_id == "0":
        print("已退出！")
        break
    
    try:
        # 转换商品ID为整数
        good_id = int(good_id)
        
        # 获取商品名称和价格
        good_name = input("请输入商品名：")
        price = float(input("请输入商品价格："))
        
        # 添加商品到列表
        products.append({"id": good_id, "name": good_name, "price": price})
        
        # 显示商品列表
        print("\n当前商品列表:")
        print("-" * 40)
        print(f"{'ID':<6} {'商品名称':<15} {'价格':<10}")
        print("-" * 40)
        
        for product in products:
            # 格式化显示商品信息
            format_id = str(product["id"]).zfill(6)
            format_name = product["name"]
            format_price = f'￥ {product["price"]:.2f}'
            print(f"{format_id} {format_name:<15} {format_price:<10}")
        print("-" * 40)
        print()
        
    except ValueError:
        print("输入无效，请输入有效的数字！")
