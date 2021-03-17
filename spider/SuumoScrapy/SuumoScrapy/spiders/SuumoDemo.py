import bs4
from bs4 import BeautifulSoup
import scrapy


class SuumodemoSpider(scrapy.Spider):
    name = 'SuumoDemo'

    def start_requests(self):

        root = "https://suumo.jp/jj/bukken/ichiran/JJ012FC002/?ar=030&bs=030&ekTjCd=&ekTjNm=&kb=1&kj=9&km=1&kt=9999999&ohf=0&pj=2&po=1&ra=030013&tb=0&tj=0&tt=9999999&bknlistmodeflg=2&pc=30"

        urls = []
        for i in range(1, 265):
            urls.append(root + "&pn=" + '%d' % i)

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        infoDict = {}

        soup = BeautifulSoup(response.body, "html.parser")
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

                infoDict.update({"list": tempList})
                yield infoDict
