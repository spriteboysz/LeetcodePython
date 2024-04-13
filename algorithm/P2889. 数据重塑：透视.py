#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-04-13 21:24
FileName: algorithm
Description:P2889. 数据重塑：透视.py 
"""

import pandas as pd

from common.utils import ss_to_pd


def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    return weather.pivot(index='month', columns='city', values='temperature')


if __name__ == '__main__':
    weather = ss_to_pd("""
+--------------+----------+-------------+
| city         | month    | temperature |
+--------------+----------+-------------+
| Jacksonville | January  | 13          |
| Jacksonville | February | 23          |
| Jacksonville | March    | 38          |
| Jacksonville | April    | 5           |
| Jacksonville | May      | 34          |
| ElPaso       | January  | 20          |
| ElPaso       | February | 6           |
| ElPaso       | March    | 26          |
| ElPaso       | April    | 2           |
| ElPaso       | May      | 43          |
+--------------+----------+-------------+    
    """)
    print(pivotTable(weather))
