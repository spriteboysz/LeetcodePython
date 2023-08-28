#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-08-26 22:22
FileName: common
Description:MySQL.py 
"""
import pandas as pd
from sqlalchemy import create_engine

# 定义数据库连接参数
__HOST__ = 'localhost'
__PORT__ = '3306'
__USER__ = 'root'
__PWD__ = 'www.huawei.com'


def get_engine(db='p1757'):
    url = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(
        __USER__, __PWD__, __HOST__, __PORT__, db)
    return create_engine(url)


def get_sql_table(db='p1757', table='products'):
    engine = get_engine(db)
    with engine.connect() as conn:
        return pd.read_sql_table(table, conn)


if __name__ == '__main__':
    df = get_sql_table('p1757', 'products')
    print(df)
