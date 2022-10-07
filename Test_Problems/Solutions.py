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

    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n < 0:
            x = 1 / x
            n = -n
            
        power = x
        multiplications = 1
        while n - multiplications * 2 >= 0:
            power *= power
            multiplications *= 2

        return power * self.myPow(x, n - multiplications)

    def find_all_connected_nodes(self, graph):
        self.allPaths = []
        end = len(graph) - 1

        def dfs(node, path):
            if node == end:
                self.allPaths.append(path)
                
            for nx in graph[node]:
                dfs(nx, path + [nx])
                
        dfs(0,[0])
        
        return self.allPaths

if __name__ == "__main__":
    sol  = Solution()
    # sol.sort_pancakes([1,5,4,3,2])
    test = sol.myPow(2.000, 10)
    print(test)