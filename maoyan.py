import requests
import pandas as pd
from pandas import Series, DataFrame
import numpy as np

baseUrl = 'http://m.maoyan.com/mmdb/comments/movie/1203084.json?_v_=yes&offset='

def crawl_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 7.0; PLUS Build/NRD90M) AppleWebKit/537.36'
                      ' (KHTML, like Gecko) Chrome/61.0.3163.98 Mobile Safari/537.36'
    }
    response = requests.get(url,headers=headers)
    if response.status_code != 200:
        print('Page access failed.')
        return {}
    #print(type(response.json()))
    return response.json()

def parse_page(page):
    comments = page.get('cmts')
    if not comments:
        return []
    for comm in comments:
        yield [
            comm.get('id'),
            comm.get('time'),
            comm.get('score'),
            comm.get('cityName'),
            comm.get('nickName'),
            comm.get('gender'),
            comm.get('content')
        ]


def start(page_num=100):
    data = []
    for i in range(1, page_num + 1):
        url = baseUrl + str(i)
        page = crawl_page(url)
        if page:
            data.extend(parse_page(page))
    return data

columns = ['id', 'time', 'score', 'city', 'name', 'gender', 'content']
df = DataFrame(start(1000), columns=columns)
df['gender'] = np.where(df.gender==1, '男', '女')
df = df.drop_duplicates('id')
df.to_csv('comments.csv', index=False)



