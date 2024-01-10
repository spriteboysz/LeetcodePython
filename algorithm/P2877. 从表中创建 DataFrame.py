#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-01-10 23:20
FileName: common
Description:P2877. 从表中创建 DataFrame.py 
"""
from typing import List

import pandas as pd


def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    return pd.DataFrame(student_data, columns=['student_id', 'age'])


if __name__ == '__main__':
    print(createDataframe([[1, 15], [2, 11], [3, 11], [4, 20]]))
