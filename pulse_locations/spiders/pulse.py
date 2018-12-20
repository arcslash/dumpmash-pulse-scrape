# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import uuid
class PulseSpider(scrapy.Spider):
    name = 'pulse'
    allowed_domains = ['pulse.lk']
    start_urls = ['https://www.pulse.lk/everythingelse/list-for-recyclers-in-sri-lanka/']
    cred = credentials.Certificate('[SERVICEKEY.json]]')
    firebase_admin.initialize_app(cred, {
        'databaseURL' : '[FIREBASE DATABSE URL]'
    })
   
    def parse(self, response):
        dis = []
        entries = []
        
        for districts in response.xpath('//p/span/strong/text()').extract():
            result = ''.join([i for i in districts if not (i.isdigit() or i == ".")])
            dis.append(result.lstrip())
            yield {"title": result.lstrip()}
        print("districts",dis)
        for tbody_id,tbody in enumerate(response.xpath('//table/tbody').extract()):
            header_read = False
            for row_id,tr in enumerate(Selector(text = tbody).xpath('//tr').extract()):
                tr_val = {"id":str(uuid.uuid4()),"latitude":0,"longitude":0,"imgPath":"../../../../assets/img/Environmental-awareness.png","collector":"","contactDetails":[], "address":"","city":"","collectableMaterials":[],"district":"","contactPerson":[], "province":"Western"}
                if header_read:
                    for td_id, td in enumerate(Selector(text = tr).xpath('//td').extract()):
                        spaned = []
                        for span in enumerate(Selector(text = td).xpath('//span/text()').extract()):
                            spaned.append(span)
                            #print("span" + str(span) + " data id:" + str(td_id))
                            if td_id == 0:
                                tr_val["collector"] = span[1]
                                tr_val["district"] = dis[tbody_id]
                            elif td_id == 1:
                                if any(char.isdigit() for char in span[1]):
                                    tr_val["contactDetails"].append({"contact":span[1]})
                                else:
                                    tr_val["contactPerson"] = {"person":span[1]}
                            elif td_id == 2:
                                tr_val["address"] = span[1]
                                tr_val["city"] = span[1].split(" ")[len(span[1].split(" ")) - 1]
                            elif td_id == 3:
                                tr_val["collectableMaterials"].append({"collectable_material":span[1]})
                    print(tr_val)
                    entries.append(tr_val)
                    
                else:
                    header_read = True

        root = db.reference()
        new_user = root.child('collection').set(entries)
                        # tr_val.append(value)
                        # print("count:" + str(counter) + " value:" +  value)
                
                # if(len(tr_val) > 0):
                #     entry.append({"Institution": tr_val[0],"contact":tr_val[1],"address":tr_val[2],"material":tr_val[3],"district":dis[tbody_id]})
                #     yield {"Institution": tr_val[0],"contact":tr_val[1],"address":tr_val[2],"material":tr_val[3],"district":dis[tbody_id]}
