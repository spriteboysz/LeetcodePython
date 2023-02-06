#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023/2/6 22:59
FileName: algorithm/Leetcode进展.py
Description: 
"""

import os
import re

language = {"java": "A", "py": "B", "rb": "C", "cpp": "D", "go": "E", "js": "F"}
path = r'D:\02_CODE'


def func():

    for root, dirs, files in os.walk(path):
        for file in filter(lambda f: f.startswith("P"), files):
            for k, v in language.items():
                if file.endswith(k):
                    col = v
                    row = re.findall(r'P(\d+)', file)[0]
                    position = col + str(int(row) + 1)
                    print(position)


if __name__ == '__main__':
    func()
