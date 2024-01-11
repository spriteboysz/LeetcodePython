#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-01-10 23:43
FileName: algorithm
Description:P2881. 创建新列.py 
"""

import pandas as pd
from common.utils import ss_to_pd


def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = employees['salary'] * 2
    return employees


if __name__ == '__main__':
    data = """
+---------+--------+
| name    | salary |
+---------+--------+
| Piper   | 4548   |
| Grace   | 28150  |
| Georgia | 1103   |
| Willow  | 6593   |
| Finn    | 74576  |
| Thomas  | 24433  |
+---------+--------+
    """
    print(createBonusColumn(ss_to_pd(data)))
