#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-10-02 21:58
FileName: LCP
Description:LCR 056. 两数之和 IV - 输入二叉搜索树.py 
"""
from common.TreeNode import TreeNode


class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            nodes.append(root.val)
            dfs(root.right)

        nodes = []
        dfs(root)
        left, right = 0, len(nodes) - 1
        while left < right:
            if nodes[left] + nodes[right] < k:
                left += 1
            elif nodes[left] + nodes[right] > k:
                right -= 1
            else:
                return True
        return False


if __name__ == '__main__':
    print(Solution().findTarget(root=TreeNode.create("[8,6,10,5,7,9,11]"), k=22))
