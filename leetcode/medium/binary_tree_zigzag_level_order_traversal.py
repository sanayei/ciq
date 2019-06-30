# Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).
#
# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its zigzag level order traversal as:
# [
#   [3],
#   [20,9],
#   [15,7]
# ]


def zigzagLevelOrder(root):
    from collections import deque
    output = []

    def _helper(node):
        if node is None:
            return
        current_level = deque()
        next_level = deque()
        level = 0
        current_level.append(node)
        while len(current_level) > 0:
            ans = []
            for i in range(len(current_level)):
                n = current_level.popleft()
                ans.append(n.val)
                if n.left is not None:
                    next_level.append(n.left)
                if n.right is not None:
                    next_level.append(n.right)
            if level % 2 == 0:
                output.append(ans)
            else:
                output.append(ans[::-1])
            level += 1
            current_level = next_level

    _helper(root)
    return output