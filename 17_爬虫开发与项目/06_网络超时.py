import requests

# 导入三种网络请求的异常类
from requests.exceptions import ReadTimeout, HTTPError, RequestException

# 循环发生50次请求
for a in range(50):
    try:
        response = requests.get("https://www.baidu.com", timeout=0.1)
        # 打印响应状态码
        print(f"第{a + 1}次请求状态码: {response.status_code}")
    except ReadTimeout as rt:
        # 打印异常信息
        print(f"第{a + 1}次请求超时: {rt}")
    except HTTPError as he:
        # 打印异常信息
        print(f"第{a + 1}次请求HTTP错误: {he}")
    except RequestException as re:
        # 打印异常信息
        print(f"第{a + 1}次请求发生错误: {re}")
