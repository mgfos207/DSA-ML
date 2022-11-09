import time
from functools import lru_cache
from collections import deque

def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} with args: {args} took {str((end - start) * 1000)} mil sec")
        return result
    return wrapper

@time_it
@lru_cache
def recursive_fibonaci(num):
    if num <= 1:
        return num
    return recursive_fibonaci(num - 1) + recursive_fibonaci(num - 2)

@time_it
def fibonaci_dynamic(num):
    if num <= 1:
        return num
    mem = [0] * (num + 1)
    mem[1] = 1
    for i in range(2, num+1): #Plus 1 is due to the range not inclusive of end
        mem[i] = mem[i - 1] + mem[i - 2]

    return mem[num]

def longest_palindrome(s):
    if s == "":
        return s
    res = ""
    dp = [None for i in range(len(s))]
    for j in range(len(s)):
        for i in range(j+1):
            if i == j:
                dp[i] = True
            elif j == i+1:
                dp[i] = (s[i] == s[j])
            else:
                dp[i] = (dp[i+1] and s[i] == s[j])
            if dp[i] and j - i + 1 > len(res):
                res = s[i:j+1]
    return res

def numDecodings(s: str) -> int:
    @lru_cache(maxsize=None)
    def recursive_memo(index):
        if index == len(s):
            return 1
        
        if s[index] == '0':
            return 0

        if index == len(s) - 1:
            return 1
        
        answer = recursive_memo(index + 1)            
        if int(s[index:index + 2]) <= 26:
            answer += recursive_memo(index + 2)
    
    return recursive_memo(0)
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def rightSideView(root):
        if root is None:
            return []
        
        next_level = deque([root,])
        rightside = []
        
        while next_level:
            # prepare for the next level
            curr_level = next_level
            next_level = deque()

            while curr_level:
                node = curr_level.popleft()
                    
                # add child nodes of the current level
                # in the queue for the next level
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            
            # The current level is finished.
            # Its last element is the rightmost one.
            rightside.append(node.val)
        
        return rightside

if __name__ == "__main__":
    root = TreeNode(5)
    l1 = TreeNode(3)
    r1 = TreeNode(6)
    l2 = TreeNode(1)
    r2 = TreeNode(8)
    root.left = l1
    root.right = l2
    l1.left = l2
    r1.right = r2
    print(rightSideView(root))
    # print(numDecodings("226"))
    # l_s = longest_palindrome("cbbd")
    # print(l_s)
    # fibo = recursive_fibonaci(10)
    # print(fibo)