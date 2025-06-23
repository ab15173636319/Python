# 练习1：保存注册信息到文件
import json


def regist():
    user_tup = {}

    while True:
        try:
            startNum = int(
                input("你已进入注册页面，按除0外其它数字开始注册，按0退出。")
            )
            if startNum == 0:
                # 读取文件内容
                fr = open("regist.json", "r", encoding="utf-8")
                content = fr.read()
                content = json.loads(content)
                content.append(user_tup)
                # 启用写入模式，会先清空内容
                fw = open("regist.json", "w", encoding="utf-8")
                # 写入文件,json.dumps()将python对象转换为json字符串
                fw.write(json.dumps(content, indent=2))
                fw.close()
                fr.close()
                user_tup = {}
                break
            else:
                print("开始注册：")
                username = str(input("请输入用户名"))
                nickname = str(input("请输入昵称"))
                password = str(input("请输入密码"))
                email = str(input("请输入邮箱"))
                phone = str(input("请输入手机号"))
                user_tup["username"] = username
                user_tup["nickname"] = nickname
                user_tup["password"] = password
                user_tup["email"] = email
                user_tup["phone"] = phone
        except Exception as e:
            print(f"发生错误，{e}，注册失败，请重新注册")


# regist()


# 练习2：按拍摄日期重命名照片
import os
import formatetime


def rename_photos(path):
    """
    按拍摄日期重命名照片
    :param path: 照片路径
    :return: None
    """

    if not os.path.exists(path):
        print("路径不存在")
        return

    # 获取路径下所有照片
    photolist = os.walk(path)
    for pathStr, disName, img in photolist:
        for imgName in img:
            abs_path = os.path.join(pathStr, imgName)
            exts = os.path.splitext(abs_path)[1]
            info = os.stat(abs_path)
            rname = (
                (formatetime.formateTime(info.st_mtime))
                .replace(" ", "___")
                .replace(":", "_")
            ) + exts
            os.rename(abs_path, os.path.join(pathStr, rname))


rename_photos("C:\\Users\\34353\\Desktop\\Python\\11_文件\\pictures")
