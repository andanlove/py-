import time

import requests
import sys
from bs4 import BeautifulSoup


# url="http://www.jingcaiyuedu.com/book/15205/1.html"
# response=requests.get(url)
# response.encoding="utf-8"
# html=response.text
# # print(html)
# bf=BeautifulSoup(html,"html.parser")
# texts=bf.find_all("div",class_="panel-body")
#
# print(texts[0].text)

# url_main="http://www.jingcaiyuedu.com"
# url="http://www.jingcaiyuedu.com/book/15205.html"
# response=requests.get(url)
# response.encoding="utf-8"
# html=response.text
# div_bf=BeautifulSoup(html,"html.parser")
# div=div_bf.find_all("div",class_="panel panel-default hidden-xs")
# a_bf=BeautifulSoup(str(div[0]),"html.parser")
# a=a_bf.find_all('a')
# for i in a:
#     print(i.string,url_main+i.get('href'))


class downloader(object):
    # 初始化
    def __init__(self):
        self.url_main = "http://www.jingcaiyuedu.com"
        self.url = "http://www.jingcaiyuedu.com/book/15205.html"
        self.names = []  # 章节名
        self.urls = []  # 章节连接
        self.nums = 0  # 章节数

    # 获取下载连接
    def get_download_url(self):
        response = requests.get(url=self.url)
        response.encoding = "utf-8"
        html = response.text
        div_bf = BeautifulSoup(html, "html.parser")
        div = div_bf.find_all("div", class_="panel panel-default hidden-xs")
        a_bf = BeautifulSoup(str(div[0]), "html.parser")
        a = a_bf.find_all("a")
        self.nums = len(a[0:])
        for i in a[0:]:
            self.names.append(i.string)
            self.urls.append(self.url_main + i.get("href"))

    # 获取章节内容
    def get_contents(self, url):
        response = requests.get(url)
        response.encoding = "utf-8"
        html = response.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all("div", class_="panel-body")
        texts = texts[0].text
        return texts

    # 写入文件
    def writer(self, name, path, text):
        write_flag = True
        with open(path, 'a', encoding="utf-8") as f:
            f.write(name + '\n')
            f.writelines(text)
            f.write('\n\n')


if __name__ == "__main__":
    down = downloader()
    down.get_download_url()
    print("下载开始:")
    for i in range(down.nums):
        down.writer(down.names[i], '无上真仙.txt', down.get_contents(down.urls[i]))
        # print("已下载%.3f%%" % (float(i / down.nums)) + '\r')
        sys.stdout.write("已下载:%f%%" % (i / down.nums) + '\r')
        sys.stdout.flush()
    print("下载完成")
