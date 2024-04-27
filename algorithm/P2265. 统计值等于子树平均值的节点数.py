#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-10-23 16:16
FileName: algorithm/P2265. 统计值等于子树平均值的节点数.py
Description: 
"""
from typing import Optional

from common.TreeNode import TreeNode


class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            nonlocal cnt
            if not root:
                return 0, 0
            left = dfs(root.left)
            right = dfs(root.right)
            value = left[0] + right[0] + root.val
            count = left[1] + right[1] + 1
            if root.val == value // count:
                cnt += 1
            return value, count

        cnt = 0
        dfs(root)
        return cnt


if __name__ == '__main__':
    root = TreeNode.create("[4,8,5,0,1,null,6]")
    print(type(root))
    ret = Solution().averageOfSubtree(root)
    print(ret)
