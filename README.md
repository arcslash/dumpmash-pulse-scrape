# DumpMash Collection Points Scrape from Pulse
Scrape garbage collection point location information from pulse article.

## Useage

Install scrapy and firebase_admin

```
pip install scrapy
pip install firebase_admin


```
clone the repository and make the necessary changes in the [pulse.py](pulselocations/spiders/pulse.py)
Lines 12 [channge to firebase service file json ] and 14 [replace with firebase database]
```
git clone https://github.com/isharaux/dumpmash-pulse-scrape.git
cd dumpmash-pulse-scrape
python scrapy crawl pulse

```

