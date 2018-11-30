# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import time
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from oyoYilong.settings import db_user, db_pawd, db_host, db_port, db_name, RETRY_CONN_MYSQL
from oyoYilong.models import BaseInfo, DeviceInfo, Status
from items import BaseInfoItem, DeviceInfoItem, StatusItem


class YiLongPipeline(object):
    # 初始化 建立数据库连接
    def __init__(self):
        self.session = self.connect_sql()

    def process_item(self, item, spider):
        if isinstance(item, BaseInfoItem):
            info = BaseInfo(
                hotel_ota_url=item['hotel_ota_url'],
                hotel_id=item['hotel_id'],
                hotel_name_cn=item['hotel_name_cn'],
                hotel_name_en=item['hotel_name_en'],
                address=item['address'],
                b_latitude=item['b_latitude'],
                b_longitude=item['b_longitude'],
                g_latitude=item['g_latitude'],
                g_longitude=item['g_longitude'],
                map_source=item['map_source'],
                score=item['score'],
                comment_txt=item['comment_txt'],
                comment_tag=item['comment_tag'],
                comments_count=item['comments_count'],
                score_rank=item['score_rank'],
                contrast_hotel_count=item['contrast_hotel_count'],
                img_total=item['img_total'],
                hotel_level=item['hotel_level'],
            )
            try:
                self.session.add(info)
                self.session.commit()
            except:
                self.session.rollback()
        elif isinstance(item, DeviceInfoItem):
            info = DeviceInfo(
                contact_info=item['contact_info'],
                base_info=item['base_info'],
                hotel_intro=item['hotel_intro'],
                hotel_policy=item['hotel_policy'],
                network_facilities=item['network_facilities'],
                room_facilities=item['room_facilities'],
                hotel_service=item['hotel_service'],
                hotel_facilities=item['hotel_facilities'],
                parking_place=item['parking_place'],
            )
            try:
                self.session.add(info)
                self.session.commit()
            except:
                self.session.rollback()
        elif isinstance(item, StatusItem):
            info = Status(
                area_id=item['area_id'],
                ota_channel_en=item['ota_channel_en'],
                batch_no=item['batch_no'],
                collect_time=item['collect_time'],
                collect_status=item['collect_status'],
                collect_host=item['collect_host'],
                create_time=item['create_time'],
                update_time=item['update_time'],
                status=item['status'],
            )
            try:
                self.session.add(info)
                self.session.commit()
            except:
                self.session.rollback()
        else:
            print('itme提交失败!')

    # 连接数据库提交错误！
    @staticmethod
    def connect_sql():
        while True:
            try:
                engine = create_engine('mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8mb4'
                                       .format(db_user, db_pawd, db_host, db_port, db_name),
                                       max_overflow=500, pool_timeout=120, pool_recycle=3600, echo=False)
                db_session = sessionmaker(bind=engine)
                return db_session()
            except Exception as conn_err:
                print("数据库连接异常：{} {}秒后重新尝试连接".format(conn_err, RETRY_CONN_MYSQL))
                time.sleep(RETRY_CONN_MYSQL)
