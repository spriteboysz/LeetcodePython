#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-02-07 23:20:37
LastEditTime: 2022-02-07 23:22:44
Description: 
FilePath: 1290.二进制链表转整数.py
'''
#
# @lc app=leetcode.cn id=1290 lang=python3
#
# [1290] 二进制链表转整数
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        value = 0
        while head:
            value = value * 2 + head.val
            head = head.next
        return value

# @lc code=end
