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

import xlwings as xw

language = ["java", "py", "rb", "cpp", "c", "go", "js", "cs"]
path = r'D:\02_CODE'


def func():
    app = xw.App(visible=True, add_book=False)
    wb = app.books.open(r'D:\02_CODE\Leetcode之路.xlsx')

    for root, dirs, files in os.walk(path):
        for file in filter(lambda f: f.startswith("P"), files):
            for col, suffix in enumerate(language):
                if file.endswith(suffix):
                    row = re.findall(r'P(\d+)', file)[0]
                    wb.sheets['Sheet1'].range(int(row) + 2, col + 2).value = '√'

    wb.save()
    wb.close()
    app.quit()


if __name__ == '__main__':
    func()
