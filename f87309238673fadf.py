import requests

response = requests.get('https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=100&sid2=268')

html = response.text
num = html.find('<ul class="type06_headline">')


from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

tags = soup.find('ul',class_="type06_headline").find_all('dl')

for tag in tags:
    a = tag.find('dt').find('a')
    b = a.text.strip()
        
    if (b != "" and b != "동영상기사"):
        print("제목: " + b)
        print("링크: " + a.get('href'))
        c = tag.find('span',class_="writing")
        print("출처: " + c.text.strip())
        print("")
