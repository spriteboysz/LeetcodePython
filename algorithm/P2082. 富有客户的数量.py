#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-08-29 11:45
FileName: algorithm
Description:P2082. 富有客户的数量.py 
"""

import pandas as pd

from common.MySQL import get_sql_table


def count_rich_customers(store: pd.DataFrame) -> pd.DataFrame:
    count = store[store['amount'] > 500]['customer_id'].nunique()
    return pd.DataFrame({'rich_count': [count]})


if __name__ == '__main__':
    store = get_sql_table('p2082', 'store')
    print(count_rich_customers(store))
