from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def _helper(idx: int, tmp_candidates: list[int], total: int):
            if total == target:
                res.append(tmp_candidates.copy())
                return 

            if total > target or idx >= len(candidates):
                return 

            tmp_candidates.append(candidates[idx])
            _helper(idx, tmp_candidates=tmp_candidates, total=total + candidates[idx])
            tmp_candidates.pop()
            _helper(idx+1, tmp_candidates=tmp_candidates, total=total)

        tmp = []
        _helper(idx=0, tmp_candidates=tmp, total=0)
        return res

        


if __name__  == "__main__":
    candidates = [2, 3, 6 ,7]
    target = 7

    solution = Solution()
    result = solution.combinationSum(candidates=candidates, target=target)
    print(result)