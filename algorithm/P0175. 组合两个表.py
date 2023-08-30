#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-08-29 11:55
FileName: algorithm
Description:P0175. 组合两个表.py 
"""

import pandas as pd

from common.MySQL import get_sql_table


def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    return person.merge(address, on='personId', how='left')[['firstName', 'lastName', 'city', 'state']]


if __name__ == '__main__':
    person = get_sql_table('P0175', 'person')
    address = get_sql_table('P0175', 'address')
    print(combine_two_tables(person, address))
    print()
