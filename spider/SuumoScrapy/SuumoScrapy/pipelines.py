# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class SuumoscrapyPipeline:
    def open_spider(self, spider):
        self.f = open('SuumoDemo.csv', 'w', encoding='utf-8')
        title = ["タイトル", "詳細URL", "販売価格", "土地面積",
                 "所在地", "坪単価", "沿線・駅", "建ぺい率・容積率"]
        self.f.write(str(title)[1:-1] + "\n")

    def close_spider(self, spider):
        self.f.close()

    def process_item(self, item, spider):
        try:
            line = str(dict(item)["list"])[1:-1] + "\n"
            self.f.write(line)
        except:
            pass
        return item
