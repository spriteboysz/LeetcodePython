#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-01-10 23:34
FileName: algorithm
Description:P2880. 数据选取.py 
"""

import pandas as pd
from common.utils import ss_to_pd


def selectData(students: pd.DataFrame) -> pd.DataFrame:
    return students.loc[students["student_id"] == 101, ["name", "age"]]


if __name__ == '__main__':
    data = """
+------------+---------+-----+
| student_id | name    | age |
+------------+---------+-----+
| 101        | Ulysses | 13  |
| 53         | William | 10  |
| 128        | Henry   | 6   |
| 3          | Henry   | 11  |
+------------+---------+-----+
    """
    print(selectData(ss_to_pd(data)))
