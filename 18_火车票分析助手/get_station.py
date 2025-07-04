import re
import requests
import json
import os
from fake_useragent import UserAgent


def get_static():
    """
    获取所有车站信息
    :return:
    """
    try:
        # 发送请求获取所有车站名称
        url = "https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9346"
        response = requests.get(url, verify=True)
        print(f"请求状态码：{response.status_code}")
        # 提取车站名称
        # [\u4e00-\u9fa5]表示所有中午字符
        # [A-Z]+表示所有大写字母
        # +表示匹配一次或多次
        pattern = r"([\u4e00-\u9fa5]+)\|([A-Z]+)"
        matches = re.findall(pattern, response.text)
        # 转为字典
        station = dict(matches)

        saveFile("station.json", station)

    except Exception as e:
        print(f"获取车站信息失败：{e}")


def get_origin_sell():
    """
    获取车站起售时间
    :return:
    """
    try:

        url = "https://www.12306.cn/index/script/core/common/qss.js"
        response = requests.get(url)
        pattren = r"{[^}]+}"
        matchs = re.findall(pattren, response.text)
        sell = json.loads(matchs[0])
        saveFile("origin_sell.json", sell)

    except Exception as e:
        print(f"获取车站起售时间信息失败：{e}")


def get_ticket(from_station, to_station, time):
    """
    获取车票信息
    :param from_station: 出发站
    :param to_station: 到达站
    :param time: 出发时间
    :return:
    """
    try:
        url = "https://kyfw.12306.cn/otn/leftTicket/queryU?leftTicketDTO.train_date={}&leftTicketDTO.from_station={}&leftTicketDTO.to_station={}&purpose_codes=ADULT"
        if time == "":
            # 获取当天时间
            import datetime

            time = datetime.datetime.now().strftime("%Y-%m-%d")

        url = url.format(
            time,
            findSomeone("station.json", from_station),
            findSomeone("station.json", to_station),
        )

        headers = {
            "User-Agent": UserAgent().random,
            "cookie": "_uab_collina=175118378256731067065957; JSESSIONID=E5AC3020E42B0CA3036F0D80AECAC2BA; route=495c805987d0f5c8c84b14f60212447d; BIGipServerotn=1339621642.50210.0000; _jc_save_toStation=%u5317%u4EAC%2CBJP; _jc_save_toDate=2025-06-29; _jc_save_wfdc_flag=dc; guidesStatus=off; highContrastMode=defaltMode; cursorStatus=off; BIGipServerpassport=854065418.50215.0000; _jc_save_fromStation=%u957F%u6C99%2CCSQ; _jc_save_fromDate=2025-06-29",
        }

        response = requests.get(url, headers=headers)
        print(f"请求状态码：{response.status_code}")
        result = response.json()
        ticketInfo = result["data"]["result"]
        station = result["data"]["map"]
        print(station)

        ticket_list = []
        tl = []
        for t in ticketInfo:
            t = t.split("|")
            ticket_list.append(t)

            ticket = {}
            ticket["ticket_type"] = t[1]
            ticket["train"] = t[3]
            ticket["from_station"] = station[t[6]]
            ticket["to_station"] = station[t[7]]
            ticket["start_time"] = t[8]
            ticket["spend_time"] = t[9]
            ticket["time"] = t[10]
            ticket["business_set"] = t[32]
            ticket["first_best"] = t[33]
            ticket["first_seat"] = t[31]
            ticket["sccond_seat"] = t[30]
            ticket["soft_sleeper"] = t[23]
            ticket["soft_sleeper_best"] = t[22]
            ticket["hard_sleeper"] = t[28]
            ticket["no_seat"] = t[26]
            ticket["hard_sleeper_seat"] = t[29]

            tl.append(ticket)
        saveFile("ticket.json", tl)
    except Exception as e:
        print(f"获取车票信息失败：{e}")


# 保存文件到当前目录
def saveFile(filename, content):
    """
    保存文件
    :param filename: 文件名
    :param content: 文件内容
    :return:
    """
    try:
        # 获取当前文件的路径
        current_path = os.path.dirname(__file__)

        path = os.path.join(current_path, filename)

        # 有同名文件就输出该文件
        if os.path.exists(path):
            os.remove(path)

        with open(path, "w", encoding="utf-8") as f:
            f.write(
                json.dumps(content, ensure_ascii=False, indent=2)
            )  # ensure_ascii=False表示不使用ascii编码
        print(f"已保存到{path}")
    except Exception as e:
        print(f"保存文件失败：{e}")


def getInfo(filename):
    """
    获取信息
    :return: 车站信息字典
    """
    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data
    except Exception as e:
        print(f"获取车站信息失败：{e}")


def getAllStaticsKey(filename):
    """
    获取字典的key
    :return: 车站的key列表
    """
    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data.keys()
    except Exception as e:
        print(f"获取车站信息失败：{e}")


def findSomeone(filename, key):
    """
    在文件中查找key
    :param filename: 文件名
    :param key: 要查找的key
    :return: 找到的value
    """
    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data[key]
    except Exception as e:
        print(f"获取失败：{e}")


if __name__ == "__main__":
    get_ticket("长沙", "广州", "2025-06-30")
