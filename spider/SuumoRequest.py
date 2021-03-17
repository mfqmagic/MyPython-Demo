# -*- coding: utf-8 -*-
import os
import csv
import requests
import bs4
from bs4 import BeautifulSoup


'''サイト内容を取得'''


def getHTMLText(url, pn):
    try:
        pkv = {"pn": pn}
        hkv = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"}
        r = requests.get(url, headers=hkv, params=pkv)
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


'''住宅情報リスト作成'''


def fillHouseList(hlist, html):

    soup = BeautifulSoup(html, "html.parser")
    if soup.find("div", class_="error_pop"):
        return False

    for osusume2 in soup.findAll("div", class_="property_unit property_unit--osusume2"):
        tempList = []
        if isinstance(osusume2, bs4.element.Tag):
            content = osusume2.find("div", class_="property_unit-content")
            header = content.find("div", class_="property_unit-header")
            body = content.find("div", class_="property_unit-body")

            title = header.find("h2").find("a")

            tempList.append(title.text.replace("\n", ""))
            tempList.append("https://suumo.jp/tochi" + title.get("href"))
            for line in body.findAll("div", class_="dottable-line"):
                if isinstance(line, bs4.element.Tag):
                    for dd in line.findAll("dd"):
                        if isinstance(dd, bs4.element.Tag):
                            tempList.append(dd.text.replace("\n", ""))

            hlist.append(tempList)

    return True


'''CSVファイル出力'''


def printHouseList(hlist):

    path = os.path.split(os.path.realpath(__file__))[0]
    csv_file = open(path + '/suumo_result.csv', 'w', encoding='utf-8')
    writer = csv.writer(csv_file, lineterminator='\n')

    csvList = [["タイトル", "詳細URL", "販売価格", "土地面積",
                "所在地", "坪単価", "沿線・駅", "建ぺい率・容積率"]]
    csvList.extend(hlist)
    writer.writerows(csvList)


'''メインメソッド'''


def main():

    houseInfo = []

    url = "https://suumo.jp/jj/bukken/ichiran/JJ012FC002/?ar=030&bs=030&ekTjCd=&ekTjNm=&kb=1&kj=9&km=1&kt=9999999&ohf=0&pj=2&po=1&ra=030013&tb=0&tj=0&tt=9999999&bknlistmodeflg=2&pc=30"
    pn = 1

    while True:
        print("ページ：", pn, end='\r')
        html = getHTMLText(url, pn)
        if not fillHouseList(houseInfo, html):
            break
        pn += 1

    printHouseList(houseInfo)


main()
