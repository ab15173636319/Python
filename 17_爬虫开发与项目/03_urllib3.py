import urllib3
from urllib3.util import response

# 创建poolmannager对象
# 用于处理与线程的连接以及线程安全
http = urllib3.PoolManager()
# 发送网络请求
# response = http.request("GET", "http://www.baidu.com")
# print(response.data.decode("utf-8"))


response=http.request("POST","http://httpbin.org/post",fields={"hello":"world"})
print(response.data.decode("utf-8"))