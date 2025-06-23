import time


# 格式化时间
def formateTime(data_time):
    """
    将时间戳转换为格式化时间
    :param data_time: 时间戳
    :return: 格式化时间
    """
    # 如：将1672531200转换为2023-01-01 00:00:00
    return time.strftime("%Y年%m月%d日 %H:%M:%S", time.localtime(data_time))
