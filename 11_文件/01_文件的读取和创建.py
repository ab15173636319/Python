# 打开文件，诺不存在就创建文件
# 打开或创建文件时，默认编码方式为GBK，诺存在中文就会出现乱码，所有要将编码改为utf-8
print("打开文件")


# open(*filename,*mode,encoding)，*为必须参数
file = open("test.txt", "r+", encoding="utf-8")

# 模式：
# r：只读模式
# w：只写模式
# a：追加模式
# r+：读写模式
# w+：读写模式
# a+：读写模式,追加
# rb：二进制只读模式
# wb：二进制只写模式
# ab：二进制追加模式
# rb+：二进制读写模式
# wb+：二进制读写模式
# ab+：二进制读写模式

print(f"文件名：{file.name}")
print(f"文件模式：{file.mode}")
print(f"文件编码：{file.encoding}")
print(f"文件是否关闭？：{file.closed}")

# 关闭文件
file.close()
print(f"文件是否关闭？：{file.closed}")
