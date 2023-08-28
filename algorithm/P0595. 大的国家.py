#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-08-28 22:47
FileName: algorithm
Description:P0595. 大的国家.py 
"""

import pandas as pd

from common.MySQL import get_sql_table


def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    world = world[(world['area'] >= 3000000) | (world['population'] >= 25000000)]
    return world[['name', 'population', 'area']]


if __name__ == '__main__':
    world = get_sql_table('p0595', 'world')
    print(big_countries(world))
