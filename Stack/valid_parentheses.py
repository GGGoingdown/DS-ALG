""" 
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

---
Example :
Input: s = "()"
Output: true

"""
class Solution:
    def isValid(self, s: str) -> bool:
        close_match: dict[str, str] = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        stack: list[str] = []
        for bracket in s:
            if close_bracket := close_match.get(bracket):
                if len(stack) == 0:
                    return False 

                last_bracket = stack.pop()
                if last_bracket != close_bracket:
                    return False
            else:
                stack.append(bracket)

        return True if len(stack) == 0 else False




if __name__ == "__main__":
    from utils import ResultValidator

    v1 = ResultValidator(inputs="()", expected_result=True)
    v2 = ResultValidator(inputs="()[]{}", expected_result=True)
    v3 = ResultValidator(inputs="([{}])", expected_result=True)
    v4 = ResultValidator(inputs="(]", expected_result=False)
    v5 = ResultValidator(inputs="[", expected_result=False)  # Note: 
    solution = Solution()
    for v in [v1, v2, v3, v4, v5]:
        result = solution.isValid(v.inputs) 
        v.validate(result)