#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-10-26 22:49
FileName: common/utils.py
Description: 
"""
import re
import pandas as pd


def ss_to_pd(ss):
    col, grid = [], []
    pattern = re.compile(r'\|\s+(\S+)\s+')
    for line in filter(lambda line: line.strip().startswith("|"), ss.splitlines()):
        parts = pattern.findall(line)
        if len(col) == 0:
            col = parts
        else:
            grid.append(list(map(lambda el: int(el) if el.isdigit() else el, parts)))
    return pd.DataFrame(grid, columns=col)


if __name__ == '__main__':
    pd = ss_to_pd("""
+----------+---------+-----+--------+
| name     | species | age | weight |
+----------+---------+-----+--------+
| Tatiana  | Snake   | 98  | 464    |
| Khaled   | Giraffe | 50  | 41     |
| Alex     | Leopard | 6   | 328    |
| Jonathan | Monkey  | 45  | 463    |
| Stefan   | Bear    | 100 | 50     |
| Tommy    | Panda   | 26  | 349    |
+----------+---------+-----+--------+""")
    print(pd)
