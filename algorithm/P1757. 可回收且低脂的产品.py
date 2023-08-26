#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-08-26 21:11
FileName: algorithm
Description:P1757. 可回收且低脂的产品.py 
"""

import pandas as pd

from common.MySQL import get_sql_table


def find_products(products: pd.DataFrame) -> pd.DataFrame:
    df = products[(products['low_fats'] == 'Y') & (products['recyclable'] == 'Y')]
    return df[['product_id']]


if __name__ == '__main__':
    products = get_sql_table('p1757', 'products')
    print(products)
    print(find_products(products))
