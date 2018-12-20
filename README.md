# DumpMash Collection Points Scrape from Pulse

Change the servicekey location and firebase database location in the [pulse.py](pulselocations/spiders/pulse.py)
Lines 12[FIREBASE SERVICE FILE] and 14[FIREBASE DB URL]

## Useage

Install scrapy and firebase_admin

```
pip install scrapy
pip install firebase_admin


```

```
    git clone https://github.com/isharaux/dumpmash-pulse-scrape.git
    cd dumpmash-pulse-scrape
    python scrapy crawl pulse

```

