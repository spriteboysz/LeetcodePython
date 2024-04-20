#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-04-20 12:47
FileName: algorithm
Description:P2883. 删去丢失的数据.py 
"""

import pandas as pd
from common.utils import ss_to_pd


def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    students.dropna(subset=['name'], inplace=True)
    return students


if __name__ == '__main__':
    students = ss_to_pd("""
+------------+---------+-----+
| student_id | name    | age |
+------------+---------+-----+
| 32         | Piper   | 5   |
| 217        | None    | 19  |
| 779        | Georgia | 20  |
| 849        | Willow  | 14  |
+------------+---------+-----+
    """)
    print(dropMissingData(students))
