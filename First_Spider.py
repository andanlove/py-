# import urllib.request
# response=urllib.request.urlopen('http://www.baidu.com')
# print( response.getcode())
# print(response.read
from urllib import request

from bs4 import BeautifulSoup

url = "http://www.biqukan.com/1_1094/5403177.html"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
page = request.Request(url, headers=headers)
page_info = request.urlopen(page).read().decode("gbk")
print(page_info)
# soup = BeautifulSoup(page_info, 'html.parser')
# titles=soup.find_all('a','title')
# print(titles)
# with open("first.txt","w",encoding="utf-8") as file:
#     for title in titles:
#         file.write(title.string+'\n')
#         file.write(url+title.get('href')+'\n\n')