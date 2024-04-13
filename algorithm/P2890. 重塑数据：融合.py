#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-04-13 21:21
FileName: algorithm
Description:P2890. 重塑数据：融合.py 
"""

import pandas as pd

from common.utils import ss_to_pd


def meltTable(report: pd.DataFrame) -> pd.DataFrame:
    return report.melt(
        id_vars=["product"],
        value_vars=["quarter_1", "quarter_2", "quarter_3", "quarter_4"],
        var_name="quarter",
        value_name="sales",
    )


if __name__ == '__main__':
    report = ss_to_pd("""
+-------------+-----------+-----------+-----------+-----------+
| product     | quarter_1 | quarter_2 | quarter_3 | quarter_4 |
+-------------+-----------+-----------+-----------+-----------+
| Umbrella    | 417       | 224       | 379       | 611       |
| SleepingBag | 800       | 936       | 93        | 875       |
+-------------+-----------+-----------+-----------+-----------+
    """)
    print(meltTable(report))
