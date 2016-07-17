#!/usr/bin/env python
# coding: UTF-8
# 日本の名字を取得するスクリプト
from bs4 import BeautifulSoup
import urllib.request
from time import sleep
from tqdm import tqdm

def getSoup(url):
    req = urllib.request.Request(url)
    response = urllib.request.urlopen(req)
    html = response.read()
    soup = BeautifulSoup(html, "lxml")
    return soup

index = []
family_name = []
population = []
baseurl = "http://www.douseidoumei.net/00/sei"

for i in tqdm(range(1316)):
    if i < 10:
        soup = getSoup( baseurl + str("0") +str(i) +".html")
    else:
        soup = getSoup( baseurl + str(i) +".html")

    for tr in soup.find_all('tr'):
        j = 0
        for td in tr.find_all('td'):
            j += 1
            if j == 1:
                index.append(td.string)
            elif j == 2:
                family_name.append(td.string)
            elif j == 3:
                population.append(td.string)
    sleep(0.3)

f = open('Japanese_family_Name_List.csv', 'w') # 書き込みモードで開く

for i in range(len(index)):
    f.write(index[i]+","+family_name[i]+","+population[i]+"\n")

f.close() # ファイルを閉じる
