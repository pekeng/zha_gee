import datetime
from sqlalchemy import Column, String, create_engine, Integer, DateTime, TEXT, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from oyoYilong.settings import db_user, db_pawd, db_host, db_port, db_name

# 创建对象的基类:
Base = declarative_base()


class BaseInfo(Base):
    # 表的名字:
    __tablename__ = 'base_info'
    # 表的结构:
    id = Column(Integer, primary_key=True)
    hotel_ota_url = Column(String(2000), )
    hotel_id = Column(String(20), )
    hotel_name_cn = Column(String(255), )
    hotel_name_en = Column(String(255), )
    address = Column(String(500), )
    b_latitude = Column(String(20), )
    b_longitude = Column(String(20), )
    g_latitude = Column(String(20), )
    g_longitude = Column(String(20), )
    map_source = Column(String(20), )
    score = Column(String(20), )
    comment_txt = Column(String(20), )
    comment_tag = Column(String(20), )
    comments_count = Column(Integer, )
    score_rank = Column(Integer, )
    contrast_hotel_count = Column(Integer, )
    img_total = Column(Integer, )
    hotel_level = Column(String(100), )


class DeviceInfo(Base):
    # 表的名字:
    __tablename__ = 'device_info'
    # 表的结构:
    id = Column(Integer, primary_key=True)
    contact_info = Column(String(255), )
    base_info = Column(String(255), )
    hotel_intro = Column(String(1000), )
    hotel_policy = Column(String(1000), )
    network_facilities = Column(String(255), )
    room_facilities = Column(String(255), )
    hotel_service = Column(String(255), )
    hotel_facilities = Column(String(255), )
    parking_place = Column(String(255), )


class Status(Base):
    # 表的名字:
    __tablename__ = 'status_info'
    # 表的结构:
    id = Column(Integer, primary_key=True)
    area_id = Column(String(50), )
    ota_channel_en = Column(String(255), )
    batch_no = Column(Integer, )
    collect_time = Column(DateTime, default=datetime.datetime.now())
    collect_status = Column(Integer, )
    collect_host = Column(String(50), )
    create_time = Column(DateTime, default=datetime.datetime.now())
    update_time = Column(DateTime, default=datetime.datetime.now())
    status = Column(Integer, )


if __name__ == "__main__":
    engine = create_engine('mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'
                           .format(db_user, db_pawd, db_host, db_port, db_name), max_overflow=500)
    Base.metadata.create_all(engine)
