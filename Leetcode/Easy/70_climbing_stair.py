class Solution:
    def climbStairs(self, n: int) -> int:
        def _helper(n: int, cache: dict) -> int:
            if n <= 2:
                return n

            if n in cache:
                return cache[n]

            cache[n] = _helper(n - 1, cache=cache) + _helper(1, cache=cache)
            return cache[n]

        return _helper(n, {})


if __name__ == "__main__":
    solution = Solution()
    print(solution.climbStairs(10))
