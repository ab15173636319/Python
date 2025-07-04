import requests

r = requests.get("https://www.baidu.com")


# print(f"状态码: {r.status_code}")
# print(f"响应头: {r.headers}")
# print(f"请求地址：{r.url}")
# print(f"源码: {r.text[:100]}")
# print(f"字节流源码: {r.content[:100]}")
# print(f"cookies: {r.cookies}")


data = {"word": "python"}
url = "http://httpbin.org/post"
postr = requests.post(url, data)

print(f"状态码: {postr.status_code}")
print(f"源码: {postr.text[:100]}")
print(f"字节流源码: {postr.content[:100]}")
