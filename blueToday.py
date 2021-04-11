#크롤링 라이브러리
import requests
import re
from bs4 import BeautifulSoup
#json 파일 형식 라이브러리
import json
from collections import OrderedDict

defaultUrl = "http://www.bluetoday.net//news/"

response = requests.get('http://www.bluetoday.net//news/articleList.html?sc_sub_section_code=S2N45&view_type=sm')

response.encoding = 'euc-kr'

html = response.text

soup = BeautifulSoup(html,'html.parser')

main = soup.find_all("td",class_="list-titles")
summary = soup.find_all("td",class_="list-summary")

Urls = []
Titles = []
Summaries = []
index=0
i=0

for tag in main:
    Urls.append(defaultUrl + tag.find('a').attrs['href'])
    Titles.append('[블루투데이]'+tag.find('a').text.strip())
    index+=1
for tag in summary:
    Summaries.append(tag.find('a').text.strip())



Crawled_Data = OrderedDict()

Crawled_Data["Urls"] = Urls;
Crawled_Data["Titles"] = Titles;
Crawled_Data["Summaries"] = Summaries;



print(json.dumps(Crawled_Data,ensure_ascii = False,indent = "\t"))
