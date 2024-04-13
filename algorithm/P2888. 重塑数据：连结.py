#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-04-13 21:11
FileName: algorithm
Description:P2888. 重塑数据：连结.py 
"""

import pandas as pd

from common.utils import ss_to_pd


def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    return pd.concat([df1, df2], axis=0)


if __name__ == '__main__':
    df1 = ss_to_pd("""
+------------+---------+-----+
| student_id | name    | age |
+------------+---------+-----+
| 1          | Mason   | 8   |
| 2          | Ava     | 6   |
| 3          | Taylor  | 15  |
| 4          | Georgia | 17  |
+------------+---------+-----+    
    """)
    df2 = ss_to_pd("""
+------------+------+-----+
| student_id | name | age |
+------------+------+-----+
| 5          | Leo  | 7   |
| 6          | Alex | 7   |
+------------+------+-----+
    """)
    print(concatenateTables(df1, df2))
