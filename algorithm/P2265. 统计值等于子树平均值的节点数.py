#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-10-23 16:16
FileName: algorithm/P2265. 统计值等于子树平均值的节点数.py
Description: 
"""
from typing import Optional
from common import TreeNode


# class Solution:
#     def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
#         pass


if __name__ == '__main__':
    root = TreeNode.create("[4,8,5,0,1,null,6]")
    print(type(root))
    ret = Solution().averageOfSubtree(root)
    print(root)

