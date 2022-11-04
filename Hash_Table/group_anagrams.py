from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for s in strs:
            sort_s = "".join(sorted(s))
            result[sort_s].append(s)

        return result.values()


if __name__ == "__main__":
    s = ["eat", "tea", "tan", "ate", "nat", "bat"]
    solution = Solution()
    result = solution.groupAnagrams(strs=s)
    print(result)
