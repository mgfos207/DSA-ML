from collections import deque
class TreeNode:
    def __init__(self, val, left, right):
        self.val = val
        self.left, self.right = left, right

# Time - O(n) | Space - O(n)
def bfs(root):
    q, ans = deque([root]), []
    while q:
        curlv, lvlen = [], len(q)
        for _ in range(lvlen):
            curn = q.popleft()
            curlv.append(curn.val)
            if curn.left: q.append(curn.left)
            if curn.right: q.append(curn.right)
            ans.append(curlv)
    return ans