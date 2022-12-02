class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        def _helper(new_stones) -> int:
            if len(new_stones) == 0:
                return 0
            if len(new_stones) == 1:
                return new_stones[0]

            new_stones = sorted(new_stones)
            stone1, stone2 = new_stones.pop(), new_stones.pop()
            if stone1 == stone2:
                return _helper(new_stones)

            new_stones.append(stone1 - stone2)
            return _helper(new_stones)

        return _helper(stones)


if __name__ == "__main__":
    stones = [2, 7, 4, 1, 8, 1]
    solution = Solution()
    result = solution.lastStoneWeight(stones)

    print(result)
