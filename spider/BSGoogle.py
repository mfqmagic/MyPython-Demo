# python 3.8.5
# -*- coding: utf-8 -*-
import csv
import os
import random
from urllib.parse import quote
from urllib.request import Request, urlopen

from bs4 import BeautifulSoup

# 検索キーワード
keyword = "証券"
# googleサイト
url = 'http://www.google.com.hk/search?hl=ja&gbv=1&q={}&start={}&sa=N'

# User-Agent
my_headers = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134",
	"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
	"Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
	"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0"]

'''HTTPアクセス'''
def getContent(myUrl):
    random_header = random.choice(my_headers)

    req = Request(myUrl)
    req.add_header("User-Agent", random_header)
    req.add_header("GET", myUrl)
    req.add_header("Host", "www.google.com")
    req.add_header("Referer", "https://www.google.com/")

    content = urlopen(req).read().decode("utf-8")
    return content


'''クローラ'''
def search(pageCnt):
    # サイトレスポンス
    myUrl = url.format(quote(keyword, 'utf-8'), pageCnt)
    result = getContent(myUrl)
    soup = BeautifulSoup(result, 'html.parser')

    # 項目
    itemList = soup.select('div .BNeawe.vvjwJb.AP7Wnd')
    # URL
    linkList = soup.select('a[href^="/url?q="]')
    # CSV出力用
    resultList = []
    for link in linkList:
        for item in itemList:
            if (item.text in link.text):
                line = []
                # 項目
                line.append(item.text.strip())
                # URL
                href = link.get('href')
                # 【/url?q=】から、【&】まで
                href = href[7:href.index("&")]
                line.append(href)

                resultList.append(line)
                break
    return resultList

# CSV内容（前2ページ）
csvList = []
for i in range(0, 20, 10):
    csvList = csvList + search(i)

# CSV出力処理
path = os.path.split(os.path.realpath(__file__))[0]
csvFile = open(path + '/result.csv', 'w', encoding='utf-8')
writer = csv.writer(csvFile, lineterminator='\n')
writer.writerows(csvList)
csvFile.close()
