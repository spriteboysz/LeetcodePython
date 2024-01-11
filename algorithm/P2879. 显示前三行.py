#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-01-10 23:28
FileName: common
Description:P2879. 显示前三行.py 
"""

import pandas as pd
from common.utils import ss_to_pd


def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.head(3)


if __name__ == '__main__':
    data = """
+-------------+-----------+-----------------------+--------+
| employee_id | name      | department            | salary |
+-------------+-----------+-----------------------+--------+
| 3           | Bob       | Operations            | 48675  |
| 90          | Alice     | Sales                 | 11096  |
| 9           | Tatiana   | Engineering           | 33805  |
| 60          | Annabelle | InformationTechnology | 37678  |
| 49          | Jonathan  | HumanResources        | 23793  |
| 43          | Khaled    | Administration        | 40454  |
+-------------+-----------+-----------------------+--------+
    """
    print(selectFirstRows(ss_to_pd(data)))
