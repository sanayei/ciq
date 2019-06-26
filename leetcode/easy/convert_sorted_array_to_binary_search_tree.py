# Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
#
# For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
#
# Example:
#
# Given the sorted array: [-10,-3,0,5,9],
#
# One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:
#
#       0
#      / \
#    -3   9
#    /   /
#  -10  5


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def sortedArrayToBST(nums):
    def _createTree(arr):
        if len(arr) == 0:
            return None
        mid = len(arr) // 2
        node = TreeNode(arr[mid])
        node.left = _createTree(arr[:mid])
        node.right = _createTree(arr[mid + 1:])
        return node

    return _createTree(nums)

if __name__ == '__main__':
    nums = [-10, -3, 0, 5, 9]
    tree = sortedArrayToBST(nums)