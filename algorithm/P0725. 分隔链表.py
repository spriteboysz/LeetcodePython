#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-08 22:46:00
LastEditTime: 2022-04-08 22:50:07
Description: 
FilePath: 725.分隔链表.py
"""
#
# @lc app=leetcode.cn id=725 lang=python3
#
# [725] 分隔链表
#

# @lc code=start
from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def splitListToParts(self, head: ListNode, k: int) -> List[ListNode]:
        cur, n = head, 0
        while cur:
            n += 1
            cur = cur.next
        each, remain = divmod(n, k)
        cur, parts, index = head, [None] * k, 0
        while cur:
            parts[index] = cur
            last = None
            for _ in range(each + (index < remain)):
                last = cur
                cur = cur.next
            index += 1
            last.next = None
        return parts

# @lc code=end
