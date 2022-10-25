class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        lookup = {
            "(": ")",
            "{": "}",
            "[": "]"
        }
        for idx in range(len(s)):
            close_bracket = lookup.get(s[idx])
            if close_bracket:
                stack.append(close_bracket)
            else:
                if len(stack):
                    close_bracket = stack.pop()
                    if close_bracket != s[idx]:
                        return False
                else:
                    return False
        
        return True if len(stack) == 0 else False


def main():
    solution = Solution()
    test1 = "["
    assert solution.isValid(test1) == False, "Error test1"
    test2 = "]"
    assert solution.isValid(test2) == False, "Error test2"
    test3 = "[{}]"
    assert solution.isValid(test3) == True, "Error test3"
    test4 = "()[]"
    assert solution.isValid(test4) == True, "Error test4"

main()