#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-04-13 21:15
FileName: algorithm
Description:P2886. 改变数据类型.py 
"""

import pandas as pd

from common.utils import ss_to_pd


def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    students = students.astype({'grade': int})
    return students


if __name__ == '__main__':
    students = ss_to_pd("""
+------------+------+-----+-------+
| student_id | name | age | grade |
+------------+------+-----+-------+
| 1          | Ava  | 6   | 73.0  |
| 2          | Kate | 15  | 87.0  |
+------------+------+-----+-------+
    """)
    changeDatatype(students)
