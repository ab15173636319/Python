import urllib.request

# 导入解析模块
import urllib.parse

data = bytes(urllib.parse.urlencode({"hello": "world"}), encoding="utf-8")
# 发送post请求
response = urllib.request.urlopen("http://httpbin.org/post", data=data)
print(response.read().decode("utf-8"))
