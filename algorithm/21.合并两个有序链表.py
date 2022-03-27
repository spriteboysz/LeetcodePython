#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-17 23:16:35
LastEditTime: 2022-03-26 21:58:04
Description: 
FilePath: 21.合并两个有序链表.py
"""
#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 and l2:
            if l1.val > l2.val:
                l1, l2 = l2, l1
            l1.next = self.mergeTwoLists(l1.next, l2)
        return l1 or l2


# @lc code=end
if __name__ == "__main__":
    s = Solution()
    l = s.mergeTwoLists([4, 5, 6], [1, 2, 3, 4])
    print(l)
