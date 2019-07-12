# Given a binary tree, collect a tree's nodes as if you were doing this: Collect and remove all leaves, repeat until the tree is empty.
#
# Example:
#
# Input: [1, 2, 3, 4, 5]
#
# Input: [1, 2, 3, 4, 5]
#
#         1
#         / \
#             2
#     3
#     / \
#         4
# 5
#
# Output: [[4, 5, 3], [2], [1]]
#

def findLeaves(root):
    from collections import defaultdict
    height = defaultdict(list)

    def helper(node):
        if node is None:
            return 0
        else:
            h = 1 + max(helper(node.left), helper(node.right))
        height[h].append(node.val)
        return h

    helper(root)
    return [height[i] for i in height.keys()]