#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-08-29 10:03
FileName: algorithm
Description:P1068. 产品销售分析 I.py 
"""

import pandas as pd

from common.MySQL import get_sql_table


def sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    return pd.merge(sales, product,
                    on='product_id'
                    )[['product_name', 'year', 'price']]


if __name__ == '__main__':
    sales = get_sql_table("P1068", "sales")
    product = get_sql_table("P1068", "product")
    print(sales_analysis(sales, product))
