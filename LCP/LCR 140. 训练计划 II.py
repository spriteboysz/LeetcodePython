#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-10-03 22:18
FileName: LCP
Description:LCR 140. 训练计划 II.py 
"""
from typing import Optional

from common.ListNode import ListNode


class Solution:
    def trainingPlan(self, head: Optional[ListNode], cnt: int) -> Optional[ListNode]:
        fast, slow = head, head
        while cnt:
            fast = fast.next
            cnt -= 1
        while fast:
            fast = fast.next
            slow = slow.next
        return slow


if __name__ == '__main__':
    print(Solution().trainingPlan(ListNode.create("[2,4,7,8]"), 1))
