import unittest
import time
from functools import lru_cache

def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} with args: {args} took {str((end - start) * 1000)} mil sec")
        return result
    return wrapper
class SantaCookies:
    def __init__(self):
        pass
    
    @time_it
    def get_cookies(self, i, nums, memo, count=None):
        curr_num = None
        try:
            curr_num = nums[i]
        except:
            curr_num = "out of bounds"
        print(f"Current index: {i}, Current num: {curr_num}, One or Two Indexes Ahead: {count}, Length of Array: {len(nums)}")
        # No more houses left to examine.
        if i >= len(nums):
            print("No more houses left to examine")
            # print(i, len(nums))
            return 0
        
        # Return cached value.
        if i in memo:
            print("Cached the result")
            return memo[i]
        
        # Recursive relation evaluation to get the optimal answer.
        ans = max(self.get_cookies(i + 1, nums, memo, "plus 1"), self.get_cookies(i + 2, nums, memo, "plus 2") + nums[i])
        # print(ans, i, nums[i])
        print("The answer and index", ans, i)
        # Cache for future use.
        memo[i] = ans
        return ans

class TestSantaCookies(unittest.TestCase):
    def test_santa_cookies(self):
        santa_cookies = SantaCookies()
        self.assertEqual(santa_cookies.get_cookies(0, [2,1,4,5], {}), 7)

if __name__ == "__main__":
    unittest.main()