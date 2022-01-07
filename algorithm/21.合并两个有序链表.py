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
        l1 = l1 + l2
        for i in range(0, len(l1)):
            for j in range(i + 1, len(l1)):
                if l1[i] > l1[j]:
                    l1[i], l1[j] = l1[j], l1[i]
        return l1


# @lc code=end
if __name__ == '__main__':
    s = Solution()
    l = s.mergeTwoLists([4, 5, 6], [1, 2, 3, 4])
    print(l)
