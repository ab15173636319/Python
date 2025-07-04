import requests


# 替换为实际可用的代理IP
proxies = {
    "http": "http://proxy.example.com:8080",
    "https": "http://proxy.example.com:8080",
}

r = requests.get("https://whatismyipaddress.com/", proxies=proxies)
# print(r.content.decode("utf-8"))
