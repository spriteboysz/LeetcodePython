#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-01-09 23:20
FileName: algorithm
Description:P2891. 方法链.py 
"""

import pandas as pd
from common.utils import ss_to_pd


def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    return animals[animals['weight'] > 100].sort_values(by='weight', ascending=False)[['name']]


if __name__ == '__main__':
    animals = ss_to_pd("""
+----------+---------+-----+--------+
| name     | species | age | weight |
+----------+---------+-----+--------+
| Tatiana  | Snake   | 98  | 464    |
| Khaled   | Giraffe | 50  | 41     |
| Alex     | Leopard | 6   | 328    |
| Jonathan | Monkey  | 45  | 463    |
| Stefan   | Bear    | 100 | 50     |
| Tommy    | Panda   | 26  | 349    |
+----------+---------+-----+--------+
    """)
    print(findHeavyAnimals(animals))
