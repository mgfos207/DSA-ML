from typing import List
from collections import Counter
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.allPaths = []
        end = len(graph) - 1

        def dfs(node, path):
            if node == end:
                self.allPaths.append(path)
                
            for nx in graph[node]:
                print(nx, node)
                dfs(nx, path + [nx])
                
        dfs(0,[0])
        
        return self.allPaths

if __name__ == "__main__":
    sol = Solution()
    sol.allPathsSourceTarget([[4,3,1],[3,2,4],[3],[4],[]])
    print(sol.allPaths)

