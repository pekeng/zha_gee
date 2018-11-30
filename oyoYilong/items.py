# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BaseInfoItem(scrapy.Item):
    # define the fields for your item here like:
    hotel_ota_url=scrapy.Field()
    hotel_id=scrapy.Field()
    hotel_name_cn=scrapy.Field()
    hotel_name_en=scrapy.Field()
    address=scrapy.Field()
    b_latitude=scrapy.Field()
    b_longitude=scrapy.Field()
    g_latitude=scrapy.Field()
    g_longitude=scrapy.Field()
    map_source=scrapy.Field()
    score=scrapy.Field()
    comment_txt=scrapy.Field()
    comment_tag=scrapy.Field()
    comments_count=scrapy.Field()
    score_rank=scrapy.Field()
    contrast_hotel_count=scrapy.Field()
    img_total=scrapy.Field()
    hotel_level=scrapy.Field()


class DeviceInfoItem(scrapy.Item):
    # define the fields for your item here like:
    contact_info=scrapy.Field()
    base_info=scrapy.Field()
    hotel_intro=scrapy.Field()
    hotel_policy=scrapy.Field()
    network_facilities=scrapy.Field()
    room_facilities=scrapy.Field()
    hotel_service=scrapy.Field()
    hotel_facilities=scrapy.Field()
    parking_place=scrapy.Field()

class StatusItem(scrapy.Item):
    # define the fields for your item here like:
    area_id=scrapy.Field()
    ota_channel_en=scrapy.Field()
    batch_no=scrapy.Field()
    collect_time=scrapy.Field()
    collect_status=scrapy.Field()
    collect_host=scrapy.Field()
    create_time=scrapy.Field()
    update_time=scrapy.Field()
    status=scrapy.Field()