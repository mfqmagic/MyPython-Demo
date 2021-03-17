# spider
### ライブラリインストール
- `pip install bs4`
- `pip install scrapy`
### 結果ファイル
- `*_result.csv`
### scrapyフレームワーク
- `scrapy startproject SuumoScrapy`
- `cd SuumoScrapy`
- `scrapy genspider SuumoDemo suumo.jp`
- 生成したSuumoDemo.pyを開発
- pipelines.pyを開発
- settings.pyのITEM_PIPELINESを設定
- `scrapy crawl SuumoDemo`