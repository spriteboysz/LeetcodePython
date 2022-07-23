#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-02-12 18:13:57
LastEditTime: 2022-02-12 18:50:59
Description: 
FilePath: 1604.警告一小时内使用相同员工卡大于等于三次的人.py
'''
#
# @lc app=leetcode.cn id=1604 lang=python3
#
# [1604] 警告一小时内使用相同员工卡大于等于三次的人
#

from collections import defaultdict
# @lc code=start
from typing import List

class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        records = defaultdict(list)
        for name, time in zip(keyName, keyTime):
            hour, minitue = map(int, time.split(":"))
            records[name].append(60 * hour + minitue)
        alertnames = []
        for name, record in records.items():
            record.sort()
            for i in range(2, len(record)):
                if record[i] - record[i - 2] <= 60:
                    alertnames.append(name)
                    break
        return sorted(alertnames)
# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.alertNames(keyName=["daniel", "daniel", "daniel", "luis", "luis", "luis", "luis"], keyTime=[
          "10:00", "10:40", "11:00", "09:00", "11:00", "13:00", "15:00"]))
    print(s.alertNames(keyName=["alice", "alice", "alice", "bob", "bob", "bob", "bob"], keyTime=[
          "12:01", "12:00", "18:00", "21:00", "21:20", "21:30", "23:00"]))
    print(s.alertNames(keyName=["john", "john", "john"], keyTime=[
          "23:58", "23:59", "00:01"]))
    print(s.alertNames(keyName=["leslie", "leslie", "leslie", "clare", "clare", "clare", "clare"], keyTime=[
          "13:00", "13:20", "14:00", "18:00", "18:51", "19:30", "19:49"]))
