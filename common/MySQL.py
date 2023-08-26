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

HOST, PORT = 'localhost', '3306'
USER, PASSWORD = 'root', '123456'


def get_sql_table(db='p1757', table='products'):
    url = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USER, PASSWORD, HOST, PORT, db)
    engine = create_engine(url)
    with engine.connect() as conn:
        products = pd.read_sql_table(table, conn)
        return products


if __name__ == '__main__':
    df = get_sql_table('p1757', 'products')
    print(df)
