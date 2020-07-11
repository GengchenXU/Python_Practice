'''
@Description: 
@Autor: GengchenXu
@Date: 2020-04-26 23:11:35
@LastEditTime: 2020-04-26 23:11:37
'''
"""
爬虫实战案例 爬取赶集网租房信息
简单来说：爬虫就是请求网站并提取数据的自动化程序
1. 发送请求 request
2. 获取响应内容 response
3. 解析内容
4.  保存数据

1. 网页文本
2. 图片
3  视频
4  其他  看的到的都可以获取

re xpath


"""
import requests
from requests.exceptions import RequestException
import re
import json


def get_page(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
    except RequestException:
        return None


def parse_page(html):
    houses = re.findall(r"""
            <div.+?ershoufang-list".+?<a.+?js-title.+?>(.+?)</a> # 获取房源的标题
            .+?<dd.+?dd-item.+?<span>(.+?)</span>  # 获取房源户型
            .+?<span.+?<span>(.+?)</span>  # 房源面积
            .+?<div.+?price.+?<span.+?>(.+?)<.span>  # 获取房源价格      
    """, html, re.VERBOSE | re.DOTALL)
    for house in houses:
        yield {
            "title": house[0],
            "house_type": house[1],
            "acreage": house[2],
            "price": house[3]
        }


def save_data(content):
    with open("ershoufang.txt", "a", encoding="utf-8")as f:
        f.write(json.dumps(content, ensure_ascii=False)+"\n")


def main():
    base_url = "http://hengyang.ganji.com/zufang/pn{}/"
    for x in range(1,11):
        url = base_url.format(x)
        html = get_page(url)
        for itme in parse_page(html):
            print(itme)
            save_data(itme)


if __name__ == '__main__':
    main()


