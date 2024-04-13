#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-04-13 21:02
FileName: algorithm
Description:P2884. 修改列.py 
"""

import pandas as pd
from common.utils import ss_to_pd


def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees['salary'] = employees['salary'] * 2
    return employees


if __name__ == '__main__':
    employees = ss_to_pd("""
+---------+--------+
| name    | salary |
+---------+--------+
| Jack    | 19666  |
| Piper   | 74754  |
| Mia     | 62509  |
| Ulysses | 54866  |
+---------+--------+
    """)
    print(modifySalaryColumn(employees))
