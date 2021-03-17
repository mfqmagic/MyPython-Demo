# python 3.8.5
# -*- coding: utf-8 -*-
import csv
import os
import random
from urllib.parse import quote
from urllib.request import Request, urlopen

from bs4 import BeautifulSoup


'''HTTPアクセス'''


def get_content(my_url):
    # User-Agent
    MY_HEADERS = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0"]
    random_header = random.choice(MY_HEADERS)

    req = Request(my_url)
    req.add_header("User-Agent", random_header)
    req.add_header("GET", my_url)
    req.add_header("Host", "www.google.com")
    req.add_header("Referer", "https://www.google.com/")

    return urlopen(req).read().decode("utf-8")


'''キーワードを検索'''


def search(key_word, page_cnt):
    # googleサイト
    URL = 'http://www.google.com.hk/search?hl=ja&gbv=1&q={}&start={}&sa=N'

    # サイトレスポンス
    my_url = URL.format(quote(key_word, 'utf-8'), page_cnt)
    result = get_content(my_url)
    soup = BeautifulSoup(result, 'html.parser')

    # 項目
    item_list = soup.select('div .BNeawe.vvjwJb.AP7Wnd')
    # URL
    link_list = soup.select('a[href^="/url?q="]')
    # CSV出力用
    result_list = []
    for link in link_list:
        for item in item_list:
            if (item.text in link.text):
                line = []
                # 項目
                line.append(item.text.strip())
                # URL
                href = link.get('href')
                # 【/url?q=】から、【&】まで
                href = href[7:href.index("&")]
                line.append(href)

                result_list.append(line)
                break
    return result_list


'''CSVファイルを出力'''


def csv_output(csv_list):
    path = os.path.split(os.path.realpath(__file__))[0]
    csv_file = open(path + '/google_result.csv', 'w', encoding='utf-8')
    writer = csv.writer(csv_file, lineterminator='\n')
    writer.writerows(csv_list)
    csv_file.close()


'''メインメソッド'''


def main(key_word):
    csv_list = []
    for page_cnt in range(0, 20, 10):
        # キーワードを検索
        csv_list.extend(search(key_word, page_cnt))

    csv_output(csv_list)


# googleからキーワードを検索してから、csvファイルを出力する
main("証券")
