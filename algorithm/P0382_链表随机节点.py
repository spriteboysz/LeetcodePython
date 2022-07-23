#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-06 21:50:38
LastEditTime: 2022-04-06 21:53:23
Description: 
FilePath: 382.链表随机节点.py
"""
#
# @lc app=leetcode.cn id=382 lang=python3
#
# [382] 链表随机节点
#

from random import randint
# @lc code=start
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def __init__(self, head: Optional[ListNode]):
        self.values = []
        while head:
            self.values.append(head.val)
            head = head.next

    def getRandom(self) -> int:
        return self.values[randint(0, len(self.values) - 1)]


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
# @lc code=end
