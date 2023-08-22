from bs4 import BeautifulSoup, NavigableString
import requests
import pandas as pd
import datetime

result = []
for page in range(1, 52):
    subway_url = 'https://www.subway.co.kr/storeSearch?page=%d&rgn1Nm=&rgnNm=#storeList' % page
    headers = {
        'user agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, likeGecko) Chrome / 100.0.4896.75Safari / 537.36'
    }
    print(subway_url)
    html = requests.get(subway_url)
    if html.status_code != 200:
        print('status_code : ', html.status_code)

    soupSubway = BeautifulSoup(html.text, 'html.parser')
    tag_tbody = soupSubway.find_all('tbody')
    print(len(tag_tbody))
    tag_tr = soupSubway.find_all('tr')
    print(len(tag_tr))
    for i in range(1, len(tag_tr)):
        for store in tag_tr[i]:
            print("i = ", i, '\n', tag_tr[i])
            tag_td = store.find_all('td') #NavigableString이라고 뜨는 곳
            print(tag_td)
            store_num = store[0]
            store_name = store[1].string
            store_address = store[2].string
            store_hour = store.select_one('store_td[3] > div > .span')
            if store_hour == "on":
                store_24 = 'YES'
            else:
                store_24 = 'NO'
            store_phone = store[4].string
            print([store_num, store_name, store_address, store_24, store_phone])
            result.append([store_num, store_name, store_address, store_24, store_phone])