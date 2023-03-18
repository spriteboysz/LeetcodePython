#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023/2/6 22:59
FileName: algorithm/Leetcode之路.py
Description: 
"""

import os
import re
from collections import defaultdict

import xlwings as xw

language = ["java", "py", "rb", "cpp", "c", "go", "js", "cs"]
path = r'D:\02_CODE'


def func():
    record = defaultdict(lambda: [""] * 8000)
    for root, dirs, files in os.walk(path):
        for file in filter(lambda f: f.startswith("P"), files):
            for col, suffix in enumerate(language):
                if file.endswith(suffix):
                    row = int(re.findall(r'P(\d+)', file)[0]) - 1
                    record[col][row] = '√'
                    break

    app = xw.App(visible=True, add_book=False)
    wb = app.books.open(r'D:\02_CODE\Leetcode之路.xlsx')
    for col, v in record.items():
        wb.sheets['Sheet1'].range(chr(ord("B") + col) + "3").options(transpose=True).value = v

    wb.save()
    wb.close()
    app.quit()


if __name__ == '__main__':
    func()
