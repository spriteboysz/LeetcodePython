#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-01 22:46:46
LastEditTime: 2022-03-01 22:48:59
Description: 
FilePath: 234.回文链表.py
"""


#
# @lc app=leetcode.cn id=234 lang=python3
#
# [234] 回文链表
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        nums = []
        cur = head
        while cur:
            nums.append(cur.val)
            cur = cur.next

        return nums == nums[::-1]

# @lc code=end
