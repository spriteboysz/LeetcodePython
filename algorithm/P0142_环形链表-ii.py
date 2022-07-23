#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-19 23:07:55
LastEditTime: 2022-04-19 23:08:17
Description: 
FilePath: 142.环形链表-ii.py
"""
#
# @lc app=leetcode.cn id=142 lang=python3
#
# [142] 环形链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow, fast = head, head
        while True:
            if not fast or not fast.next:
                return None
            slow, fast = slow.next, fast.next.next
            if slow == fast:
                break
        fast = head
        while slow != fast:
            fast, slow = fast.next, slow.next
        return fast


# @lc code=end
