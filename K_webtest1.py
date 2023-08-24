import requests
from bs4 import BeautifulSoup

def crawl_blog_info(search_keyword):
    url = f"https://search.naver.com/search.naver?where=view&sm=tab_jum&query={search_keyword}"
    
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        blog_list = soup.find_all("li", class_="bx")
        
        for blog in blog_list:
            blog_info = blog.find("a", class_="api_txt_lines total_tit")
            if blog_info:
                blog_name = blog_info.get_text()
                blog_link = blog_info["href"]
                posting_date = blog.find("span", class_="sub_time").get_text()
                
                print("블로그명:", blog_name)
                print("블로그글의 주소:", blog_link)
                print("포스팅 날짜:", posting_date)
                print("------------------------")
    else:
        print("Failed to retrieve the webpage.")

# 검색 키워드를 입력하세요.
search_keyword = input("검색할 키워드를 입력하세요: ")
crawl_blog_info(search_keyword)
