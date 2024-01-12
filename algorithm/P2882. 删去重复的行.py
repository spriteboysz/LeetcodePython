#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-01-11 23:24
FileName: algorithm
Description:P2882. 删去重复的行.py 
"""

import pandas as pd
from common.utils import ss_to_pd


def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    customers.drop_duplicates(subset='email', keep='first', inplace=True)
    return customers


if __name__ == '__main__':
    data = """
+-------------+---------+---------------------+
| customer_id | name    | email               |
+-------------+---------+---------------------+
| 1           | Ella    | emily@example.com   |
| 2           | David   | michael@example.com |
| 3           | Zachary | sarah@example.com   |
| 4           | Alice   | john@example.com    |
| 5           | Finn    | john@example.com    |
| 6           | Violet  | alice@example.com   |
+-------------+---------+---------------------+
    """
    print(dropDuplicateEmails(ss_to_pd(data)))
