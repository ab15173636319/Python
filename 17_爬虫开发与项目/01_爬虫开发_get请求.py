import urllib.request


# =============================跳过get请求获取指定页面内容=============================

# 1.确定url路径
url = "https://www.baidu.com"

# 打开指定需要爬取的网页
response = urllib.request.urlopen(url)
# 读取网页代码
html = response.read().decode("utf-8")

# 创建或保存到本地文件
with open("baidu.html", "w", encoding="utf-8") as f:
    f.write(html)
