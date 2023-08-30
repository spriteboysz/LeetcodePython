#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-08-29 11:30
FileName: algorithm
Description:P0620. 有趣的电影.py 
"""
import pandas as pd

from common.MySQL import get_sql_table


def not_boring_movies(cinema: pd.DataFrame) -> pd.DataFrame:
    return cinema[(cinema['id'] % 2 == 1) & (cinema['description'] != 'boring')].sort_values(by='rating',
                                                                                             ascending=False)


if __name__ == '__main__':
    cinema = get_sql_table('P0620', 'cinema')
    print(not_boring_movies(cinema))
