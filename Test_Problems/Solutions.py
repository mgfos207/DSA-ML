from typing import List
class Solution:
    def sort_pancakes(self, arr: List[int]) -> List[int]:
        
        def get_max_val_idx(arr: List[int]) -> int:
            m_idx = -1
            m_val = float('-inf')

            for idx, num in enumerate(arr):
                if num > m_val:
                    m_val = num
                    m_idx = idx

            return m_idx

        def flip(arr, k):
            i = 0
            while k > i:
                arr[i], arr[k] = arr[k], arr[i]
                i += 1
                k -= 1
            print(arr)
            return arr

        i = len(arr) - 1

        while i > 0:
            m_idx = get_max_val_idx(arr[:i + 1])
            arr = flip(arr, m_idx)
            arr = flip(arr, len(arr[:i + 1]) - 1)

            i -= 1


if __name__ == "__main__":
    sol  = Solution()
    sol.sort_pancakes([1,5,4,3,2])
