import unittest
from typing import List
class StairClimbCost:
    def __init__(self):
        self.dp = None
        pass

    def solution(self, cost: List[int]) -> int:
        if len(cost) == 2:
            return min(cost[0], cost[1])

        self.dp = [0] * (len(cost) + 1)
        
        for i in range(2, len(cost) + 1):
            self.dp[i] = min(self.dp[i -1 ] + cost[i - 1], self.dp[i - 2] + cost[i - 2])
        
        return self.dp[-1]            


class TestStairClimb(unittest.TestCase):
    def test_stair_climb(self):
        stair_climb_obj = StairClimbCost()
        self.assertEqual(stair_climb_obj.solution([10,15,20]), 15)
        self.assertEqual(stair_climb_obj.solution([1,100,1,1,1,100,1,1,100,1]), 6)

if __name__ == "__main__":
    unittest.main()