# 读取文件

# f = open("test.txt", "w")

# 写入
# f.write("i am the king of the world!!!\n" * 100)

# 读取
f = open("test.txt", "r")

# read()是一字节一字节地读取
content1 = f.read()

# readline()是按行读取，但只会读取一行
content2 = f.readline()

# readlines()是按行读取，会将所有行读取到一个列表中
content3 = f.readlines()

print(content1)


f.close()
