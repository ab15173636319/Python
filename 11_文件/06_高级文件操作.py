import os

# ===============================删除文件=================================
# 使用os.remove(path)
# 如：删除test1/test2/test3/test.txt
try:
    os.remove("test1/test2/test3/test.txt")
    print("删除成功")
except:
    print("删除失败")


# =================================重命名文件或目录================================
# 使用os.rename(old, new)
# 诺指定路径末为目录则修改目录名、诺为文件则修改文件名
# 如：将test.txt重命名为test1.txt
try:
    os.rename("test1/test2/test3/rename.txt", "test1/test2/test3/重命名文件.txt")
    print("重命名成功")
except:
    print("重命名失败，文件不存在")

# =================================获取文件基本信息================================
# 使用os.stat(path)
# 获取例如最后访问时间、最后一次修改时间、文件大小...
# 其会返回一个stat_result对象，包含以下属性：
# st_mode：文件权限和类型，如：0o100644表示文件权限为644，类型为普通文件
# st_ino：inode节点号，文件的唯一标识，用于索引文件
# st_dev：文件系统的设备号，文件所在的设备号
# st_nlink：硬链接数
# st_uid：用户ID
# st_gid：组ID
# st_size：文件大小（字节）
# st_atime：最后访问时间
# st_mtime：最后修改时间
# st_ctime：创建时间
# 如：获取00_example_images/1.png的基本信息

import formatetime

try:
    img_info = os.stat("00_example_images/1.png")
    print(img_info)
    # 如：获取文件大小
    print(f"该文件大小为：{img_info.st_size / 1024**2:.2f} MB")
    # 如：获取最后访问时间
    print(formatetime.formateTime(img_info.st_atime))

    # 如：获取最后修改时间
    print(formatetime.formateTime(img_info.st_mtime))
    # 如：获取创建时间
    print(formatetime.formateTime(img_info.st_ctime))
except:
    print("获取失败")
