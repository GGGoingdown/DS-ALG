# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
def guess(num: int) -> int:
    picked_num = 69
    if num > picked_num:
        return -1

    if num < picked_num:
        return 1

    return 0


class Solution:
    def guessNumber(self, n: int) -> int:
        low, high = 1, n
        while low <= high:
            mid = (low + high) // 2

            if guess(mid) < 0:
                high = mid - 1
            elif guess(mid) > 0:
                low = mid + 1
            else:
                return mid

        return mid


if __name__ == "__main__":
    solution = Solution()
    result = solution.guessNumber(100)
    print(result)