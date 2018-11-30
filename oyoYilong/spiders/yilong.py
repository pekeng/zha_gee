# -*- coding: utf-8 -*-
import json
import re
import scrapy
from scrapy import FormRequest, Request
from items import BaseInfoItem, DeviceInfoItem, StatusItem


class YilongSpider(scrapy.Spider):
    name = 'yilong'
    allowed_domains = ['elong.com']
    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",
    }

    def start_requests(self):
        url = 'http://hotel.elong.com/ajax/tmapilist/asyncsearch'
        for i in range(1, ):
            formdata = {
                "code": "7809114",
                "listRequest.areaID": "",
                "listRequest.bookingChannel": '5',
                "listRequest.cityID": "0101",
                "listRequest.pageIndex": str(i),
                "listRequest.pageSize": '20',
            }
            yield FormRequest(url, formdata=formdata, headers=self.headers)

    def parse(self, response):
        html = json.loads(response.text)
        lists = re.findall('class="h_info_base">(.*?)查看详情', html['value']['hotelListHtml'], re.S)
        print(len(lists))
        for list in lists[:2]:
            # 酒店名称
            name = re.findall('title=\"(.+?)\"><span', list)
            print(name)
            # 酒店价格
            price = re.findall('class="h_pri_num ">(.*?)</span>', list)
            # 酒店地址
            address = re.findall('data-hoteladdress="(.*)" >', list)
            hotal_dict = {
                'name': name,
                'price': price,
                'address': address,
            }
            # 酒店id
            hotelids = re.findall('class="t14" href="(.*)" target="_blank">', list)
            if hotelids:
                hotelid = hotelids[0].replace("/", '')
                parse_url = 'http://hotel.elong.com/' + hotelid
                print(parse_url)
                # meta用来传提参数，
                yield Request(url=parse_url, callback=self.parse_hotal_info, meta={
                    'hotal_dict': hotal_dict,
                    'hotelid': hotelid
                })

    # 酒店信息
    def parse_hotal_info(self, response):
        print(',,,,,,,,,,,,,,,,,,,')
        tel = response.xpath(
            "//div[@id='hotelContent']/div[@class='dview_info']/dl[@class='dview_info_item'][1]/dd/text()").extract_first().strip(
            '\n \t')
        comments = response.xpath(
            "//div[@class='hrela_comt_total']/a/text()").extract_first()
        hotal_star = response.xpath(
            "//div[@class='t24 yahei']/b/@title").extract_first()
        print(tel)
        from_data2 = {
            'code': '7836312',
            'detailRequest.checkInDate': '2018-10-27 00:00:00',
            'detailRequest.cardNo': '192928',
            'detailRequest.checkOutDate': '2018-10-28 00:00:00',
            'detailRequest.hotelIDs': response.meta['hotelid'],
            'detailRequest.isAfterCouponPrice': 'true',
            'detailRequest.orderFromID': '50',
        }
        yield FormRequest(url='http://hotel.elong.com/ajax/tmapidetail/gethotelroomsetjva',
                          callback=self.parse_room_type, formdata=from_data2)

    def parse_room_type(self, response):
        print('...........')
        print(response.text)

        """
        # 入住时间
        # 酒店设施
        # 酒店简介
        # """
        # 等你所有解析完，，一起yield,切记要一起yield!!!!!!!!!!!!!!!!!!
        item=BaseInfoItem()
        hotel_ota_url=''
        hotel_id=''
        hotel_name_cn=''
        hotel_name_en=''
        address=''
        b_latitude=''
        b_longitude=''
        g_latitude=''
        g_longitude=''
    #     map_source=''
    #     score=''
    #     comment_txt=''
    #     comment_tag=''
    #     comments_count=''
    #     score_rank=''
    #     contrast_hotel_count=''
    #     img_total=''
    #     hotel_level=''
    #     item['hotel_ota_url']=hotel_ota_url
    #     item['hotel_id']=hotel_id
    #     item['hotel_name_cn']=hotel_name_cn
    #     item['hotel_name_en']=hotel_name_en
    #     item['address']=address
    #     item['b_latitude']=b_latitude
    #     item['b_longitude']=b_longitude
    #     item['g_latitude']=g_latitude
    #     item['g_longitude']=g_longitude
    #     item['map_source']=map_source
    #     item['score']=score
    #     item['comment_txt']=comment_txt
    #     item['comment_tag']=comment_tag
    #     item['comments_count']=comments_count
    #     item['score_rank']=score_rank
    #     item['contrast_hotel_count']=contrast_hotel_count
    #     item['img_total']=img_total
    #     item['hotel_level']=hotel_level
    #     yield item
    #
    #
    # def next(self,response):
    #     # 解析下面这些，
    #     hotel_ota_url=''
    #     hotel_id=''
    #     hotel_name_cn=''
    #     hotel_name_en=''
    #     address=''
    #     b_latitude=''
    #     b_longitude=''
    #     g_latitude=''
    #     g_longitude=''
    #     item =DeviceInfoItem()
    #     item['contact_info']=hotel_ota_url
    #     item['base_info']=hotel_id
    #     item['hotel_intro']=hotel_name_cn
    #     item['hotel_policy']=hotel_name_en
    #     item['network_facilities']=address
    #     item['room_facilities']=b_latitude
    #     item['hotel_service']=b_longitude
    #     item['hotel_facilities']=g_latitude
    #     item['parking_place']=g_longitude
    #     yield item
    # def next2(self, response):
    #     area_id=''
    #     ota_channel_en=''
    #     batch_no=''
    #     collect_time=''
    #     collect_status=''
    #     collect_host=''
    #     create_time=''
    #     update_time=''
    #     status=''
    #     item=StatusItem()
    #     item['area_id']=area_id
    #     item['ota_channel_en']=ota_channel_en
    #     item['batch_no']=batch_no
    #     item['collect_time']=collect_time
    #     item['collect_status']=collect_status
    #     item['collect_host']=collect_host
    #     item['create_time']=create_time
    #     item['update_time']=update_time
    #     item['status']=status
    #     yield item
