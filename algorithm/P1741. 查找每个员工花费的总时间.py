#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-08-29 10:40
FileName: algorithm
Description:P1741. 查找每个员工花费的总时间.py 
"""
import pandas as pd

from common.MySQL import get_sql_table


def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    employees['total_time'] = employees.apply(
        lambda row: row['out_time'] - row['in_time'], axis=1
    )
    employees = employees.groupby(by=['event_day', 'emp_id'])['total_time'].sum()
    return employees.reset_index().rename(columns={'event_day': 'day'})


if __name__ == '__main__':
    employees = get_sql_table('P1741', 'employees')
    print(total_time(employees))
