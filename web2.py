#web02.py

#웹서버에 통신
import requests
#크롤링
from bs4 import BeautifulSoup

url = "https://www.daangn.com"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

posts = soup.find_all("div", attrs={"class":"card-desc"})

f = open("c:\\work\\danngn.txt", "wt", encoding="utf-8")
for post in posts:
    titleElem = post.find("h2", atttrs={"class":"card-title"})
    priceElem = post.find("div", atttrs={"class":"card-price"})
    addrElem = post.find("div", atttrs={"class":"card-region-name"}) 
    title = titleElem.text.replace("\n", "")
    price = priceElem.text.replace("\n", "")
    addr = addrElem.text.replace("\n", "")
    print(f"{title}, {price}, {addr}")


    # <div class="card-desc">
    #   <h2 class="card-title">인터프로 미사일자전거 판매</h2>
    #   <div class="card-price ">
    #     100,000원
    #   </div>
    #   <div class="card-region-name">
    #     경남 김해시 삼계동
    #   </div>
