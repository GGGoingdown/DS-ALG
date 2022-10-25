class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        needle_length = len(needle)
        if needle_length == 0:
            return 0

        if not len(haystack):
            return -1
        
        hay_stack_length = (len(haystack) - needle_length) + 1
        for i in range(hay_stack_length):
            sub_hay = haystack[i:i+needle_length]
            if sub_hay == needle:
                return i

        return -1



def main():
    haystack = ""
    needle = "bba"
    solution = Solution()
    print(solution.strStr(haystack=haystack, needle=needle))


main()


