# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import csv
import os

class ImagePipline(object):
    def process_item(self,item,spider):
        f = open('C:/Users/10338/Desktop/scrapy_data/Image.csv','a+',encoding='utf8',newline='',errors='ignore')
        writer = csv.writer(f)
        writer.writerow(item['img'].keys())
        writer.writerow(item['img'].values())
        writer.writerow(item['prices'].keys())
        writer.writerow(item['prices'].values())
        writer.writerow(dict(item['describe_dict']).keys())
        writer.writerow(dict(item['describe_dict']).values())
        writer.writerow(item['describe_Size_Inches_S'])
        writer.writerow(item['describe_Size_Inches_M'])
        writer.writerow(item['describe_Size_Inches_L'])
        writer.writerow(item['describe_Size_Cen_S'])
        writer.writerow(item['describe_Size_Cen_M'])
        writer.writerow(item['describe_Size_Cen_L'])
        return item
