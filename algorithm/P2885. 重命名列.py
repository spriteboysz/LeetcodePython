#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-01-11 23:27
FileName: algorithm
Description:P2885. 重命名列.py 
"""

import pandas as pd

from common.utils import ss_to_pd


def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    students = students.rename(
        columns={
            "id": "student_id",
            "first": "first_name",
            "last": "last_name",
            "age": "age_in_years",
        }
    )
    return students


if __name__ == '__main__':
    data = """
+----+---------+----------+-----+
| id | first   | last     | age |
+----+---------+----------+-----+
| 1  | Mason   | King     | 6   |
| 2  | Ava     | Wright   | 7   |
| 3  | Taylor  | Hall     | 16  |
| 4  | Georgia | Thompson | 18  |
| 5  | Thomas  | Moore    | 10  |
+----+---------+----------+-----+
    """
    print(renameColumns(ss_to_pd(data)))
