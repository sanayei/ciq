from collections import deque

class Node(object):
  def __init__(self, value, left=None, right=None):
    self.val = value
    self.left = left
    self.right = right

def levelOrder(root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    from collections import deque
    ans = []
    currentLevel = deque()
    if root is not None:
        currentLevel.append(root)
    while len(currentLevel) > 0:
        subans = []
        nextLevel = deque()
        for i in range(len(currentLevel)):
            n = currentLevel.popleft()
            subans.append(n.val)
            if n.left is not None:
                nextLevel.append(n.left)
            if n.right is not None:
                nextLevel.append(n.right)
        ans.append(subans)
        currentLevel = nextLevel
    return ans

if __name__ == '__main__':
    t = Node(1, Node(2, Node(4, Node(7))), Node(3, Node(5), Node(6)))

    ans = levelOrder(t)
    print(ans)