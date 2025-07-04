from bs4 import BeautifulSoup


# 获取百度热搜榜的标题
new_title = []
with open("baidu.html", "r", encoding="utf-8") as file:
    html_content = file.read()
    soup = BeautifulSoup(html_content, features="lxml")
    for link in soup.find_all("a"):
        span = link.find_all("span")
        if span:
            new_title.append(span[1].text)
print(new_title)
