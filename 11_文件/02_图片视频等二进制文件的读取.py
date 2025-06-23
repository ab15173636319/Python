# 读取图片
file_path = "00_example_images/2.jpg"
# rb----------以二进制格式打开文件，并只采用只读模式，一般用于图片、视频和音频等。
# rb+---------以二进制格式打开文件，并采用读写模式，一般用于对文件进行随机读写。
# wb----------以二进制格式打开文件，并采用只写模式，一般用于写入图片、视频和音频等。
# wb+---------以二进制格式打开文件，并采用读写模式，一般用于对文件进行随机读写。
file = open(file_path, "rb")
print(file)
file.close()

# 使用with语句，可自动关闭文件
with open(file_path, "rb") as file2:
    print(file2)
    