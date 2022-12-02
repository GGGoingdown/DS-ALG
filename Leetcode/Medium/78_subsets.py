from typing import List

""" Example:
nums: [1, 2, 3]
result: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
"""


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def explore(chosen, remaining, res):
            if not remaining:
                res.append(chosen[:])
                return
            d = remaining.pop(0)
            # choose
            chosen.append(d)
            # explore
            explore(chosen, remaining, res)
            chosen.pop()
            explore(chosen, remaining, res)
            # unchoose
            remaining.insert(0, d)

        res = []
        chosen = []
        explore(chosen, nums, res)
        return res
