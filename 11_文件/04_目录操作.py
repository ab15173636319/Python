# Python并不能进行目录操作，而是需要内置模块os来实现。

# 导入os
import os

# ===============================================================================获取当前工作目录==================================================================================
print(f"当前工作目录：{os.getcwd()}")

# listdir(path)
# 获取路径下所有目录信息，不会获取子目录
print(f"返回指定路劲下玩家和目录信息：{os.listdir('./')}")

#  mkdir(path)
# 创建文件夹,如果存在则报错
try:
    os.mkdir("test")
    print("文件夹创建成功")
except:
    print("文件已存在")

# emdir(path)
# ===========================================================删除目录=============================================================
# 删除目录
# 删除目录时，要确保目录为空，否则会报错

try:
    os.rmdir("test")
    print("文件夹删除成功")
except:
    print("文件夹删除失败，只能删除空文件夹！")

# removedirs(path1/path2...)
# 递归删除目录路径下所有空目录，诺是嵌套则非空之前所有文件夹都会被删除，诺是诺干同级子文件夹则都会被保留
# 如果目录不存在，会抛出异常。
# 如果目录不为空，会抛出异常。
# 如果删除成功，不会返回任何值。
# 如果删除失败，会抛出异常。

try:
    os.removedirs("test")
    print("文件夹删除成功")
except:
    print("文件夹删除失败！")


# chdir(path)
# 类似于shell的cd操作，切换执行文件路径
# ===========================================================改变当前工作目录=============================================================
# 改变当前工作目录
# 该方法没有返回值
# 如果路径不存在，会抛出异常。
# 如果路径为空字符串，会抛出异常。
# 如果路径为相对路径，会根据当前工作目录改变。
# 如果路径为绝对路径，会根据绝对路径改变。
# 如果路径为.，会改变当前工作目录为上级目录。
# 如果路径为..，会改变当前工作目录为上上级目录。
# 如果路径为~，会改变当前工作目录为用户主目录。


# join(path,name)
# ===========================================================拼接目录与文件名=============================================================

path_join = "./TEST"
dir_name = "test1"
dir_name2 = "test2"
file_name = "test1.txt"

print(f"拼接目录和文件：{os.path.join(path_join, file_name)}")
# 多个使用,
print(
    f"拼接目录、子目录和文件：{os.path.join(path_join, dir_name, dir_name2, file_name)}"
)

# ===========================================================分离文件名和拓展名=============================================================
# splitext()

splitext_tup = os.path.splitext(file_name)
print(f"分离文件名：{splitext_tup[0]}和扩展名：{splitext_tup[1]}")


# 判断目录是否存在？
# exists(path)

verify_path = r"..\00_example_images"

verify_path_exists = os.path.exists(verify_path)
print(f"判断目录是否存在：{verify_path_exists}")

# ===========================================================创建多级目录=============================================================

# mkdirs(path)

makedirs_path = "C:\\Users\\34353\\Desktop\\Python\\test1\\test2\\test3"

try:
    os.makedirs(makedirs_path)
    # 获取绝对路径
    print("文件夹创建成功")
except:
    print("文件已存在")

# ============================================================遍历目录=============================================================

# walk(top,topdown,onerror,followlinks)
# top：起始目录路径。
# topdown：遍历顺序（默认 True 表示自顶向下，先父目录后子目录）。
# onerror：错误处理函数（可选）。
# followlinks：是否跟随符号链接（默认 False）。

# 以列表的形式返回文件元组：
# 元组结构：
# dirpath：当前目录的路径（字符串）。
# dirnames：当前目录下的子文件夹名列表（字符串列表）。
# filenames：当前目录下的文件名列表（字符串列表）。

list = os.walk("C:\\Users\\34353\\Desktop\\Python\\test1")
print(list)
for item in list:
    print(item)
