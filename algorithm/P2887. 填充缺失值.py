#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-04-13 21:29
FileName: algorithm
Description:P2887. 填充缺失值.py 
"""

import pandas as pd

from common.utils import ss_to_pd


def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    products['quantity'].fillna(0, inplace=True)
    return products


if __name__ == '__main__':
    product = ss_to_pd("""
+-----------------+----------+-------+
| name            | quantity | price |
+-----------------+----------+-------+
| Wristwatch      | 32       | 135   |
| WirelessEarbuds | None     | 821   |
| GolfClubs       | None     | 9319  |
| Printer         | 849      | 3051  |
+-----------------+----------+-------+    
    """)
    print(fillMissingValues(product))
