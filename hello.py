# ----- 변수 & 기본연산 -----

# a = 2
# b = 3

# a = 'connie'
# b = 'park'
# print(a+b)

# ----- 자료형 -----

# a_list = ['사과','배','감']
# print(a_list[2])
# a_list.append('수박')
# print(a_list)

# a_dict = {
#     'name':'connie',
#     'age':27
# }
# print(a_dict['name'])


# ----- 함수 -----
# def sum(a,b):
#     print('더하자!')
#     return a+b
# result = sum(2,3)
# print(result)

# ----- 조건문 -----

# def is_adult(age):
#     if age > 20:
#         print('성인입니다.')
#     else:
#         print('청소년입니다.')
#
# is_adult(15)


# ----- 반복문 -----

# fruits = ['사과','배','배','감','수박','귤','딸기','사과','배','수박']
#
# # for fruit in fruits:
# #     print(fruit)
#
# count = 0
# for aaa in fruits:
#     if aaa == '사과':
#         count += 1
#
# print(count)

# people = [{'name': 'bob', 'age': 20},
#           {'name': 'carry', 'age': 38},
#           {'name': 'john', 'age': 7},
#           {'name': 'smith', 'age': 17},
#           {'name': 'ben', 'age': 27}]
#
# for person in people:
#     if person['age'] > 20:
#         print(person['name'])

# ----- requests 써보기 -----
# import requests # requests 라이브러리 설치 필요
#
# r = requests.get('http://spartacodingclub.shop/sparta_api/seoulair')
# rjson = r.json()  #requests library 쓰는 방법
#
# rows = rjson['RealtimeCityAir']['row']
#
# for row in rows:
#
#     gu_name = row['MSRSTE_NM']
#     gu_mise = row['IDEX_MVL']
#
#     # print(gu_name,gu_mise)
#
#     if gu_mise < 60:
#         print(gu_name)

import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=pnt&date=20210829',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

# title = soup.select_one('#old_content > table > tbody > tr:nth-child(2) > td.title > div > a')
# print(title['href'])

#old_content > table > tbody > tr:nth-child(3) > td.title > div > a
#old_content > table > tbody > tr:nth-child(4) > td.title > div > a

movies = soup.select('#old_content > table > tbody > tr')

# print(movies)
for movie in movies:
    a = movie.select_one('td.title > div > a')
    # print(a)
    if a is not None:
        # print(a.text)  #a에서 text값들만!
        title = a.text
        rank = movie.select_one('td:nth-child(1) > img')['alt']
        #('#old_content > table > tbody > tr:nth-child(2) > td:nth-child(1) > img') 검사-copy-copyselector에서 tr까지는 위에 이미 가지고 온 것(지워도 됨!)
        # print(rank)  #rank에서 'alt값만 갖고오면 됨' print(rank['alt']) 라고 써도 똑같음(위에 ['alt']지우고)
        star = movie.select_one('td.point') #.text여기 써도 됨!
        print(rank, title, star.text)