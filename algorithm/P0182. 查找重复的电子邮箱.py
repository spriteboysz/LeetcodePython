#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-08-29 11:38
FileName: algorithm
Description:P0182. 查找重复的电子邮箱.py 
"""

import pandas as pd

from common.MySQL import get_sql_table


def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    df = person.groupby(by='email').size().reset_index(name='count')
    return df[df['count'] > 1][['email']]


if __name__ == '__main__':
    person = get_sql_table('p0182', 'person')
    print(duplicate_emails(person))
