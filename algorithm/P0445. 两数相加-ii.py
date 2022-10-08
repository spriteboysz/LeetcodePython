#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-17 10:32:24
LastEditTime: 2022-04-17 10:49:48
Description: 
FilePath: 445.两数相加-ii.py
"""
#
# @lc app=leetcode.cn id=445 lang=python3
#
# [445] 两数相加 II
#

# @lc code=start
# Definition for singly-linked list.


# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        nodes1, nodes2 = [], []
        while l1:
            nodes1.append(l1.val)
            l1 = l1.next
        while l2:
            nodes2.append(l2.val)
            l2 = l2.next
        if len(nodes1) > len(nodes2):
            nodes2 = [0] * (len(nodes1) - len(nodes2)) + nodes2
        else:
            nodes1 = [0] * (len(nodes2) - len(nodes1)) + nodes1

        carry, nodes = 0, []
        for i in range(len(nodes1) - 1, -1, -1):
            carry, value = divmod((nodes1[i] + nodes2[i] + carry), 10)
            nodes.append(value)
        if carry:
            nodes = [carry] + nodes[::-1]
        else:
            nodes = nodes[::-1]
        print(nodes)
        cur = head = ListNode(-1)
        #cur = head 
        for node in nodes:
            temp = ListNode(node) 
            cur.next = temp 
            cur = cur.next 
        return head.next 


# @lc code=end
