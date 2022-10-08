#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-11 22:52:16
LastEditTime: 2022-04-11 22:55:42
Description: 
FilePath: 160.相交链表.py
"""
#
# @lc app=leetcode.cn id=160 lang=python3
#
# [160] 相交链表
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        a, b = headA, headB
        while a != b:
            a = a.next if a else headB
            b = b.next if b else headA
        return a


# @lc code=end
