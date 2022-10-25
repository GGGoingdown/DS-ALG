class Solution:
    def isPalindrome(self, x: int) -> bool:
        og = x
        if x < 0:
            return False
        reverted_number = 0
        while x:
            mod_number = x % 10
            reverted_number = (reverted_number * 10 ) + mod_number
            x = x//10
            print(f"X: {x} - Reverted: {reverted_number}")

        return True if reverted_number == og else False



def main():
    solution = Solution()
    x = -1
    result = solution.isPalindrome(x)
    assert result == False, f"Error result"
    x = 0
    result = solution.isPalindrome(x)
    assert result == True, f"Error result"
    x = 121
    result = solution.isPalindrome(x)
    assert result == True, f"Error result"

main()