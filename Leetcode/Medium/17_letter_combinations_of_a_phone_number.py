from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        lookup: dict[str, str] = {
            "": "",
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        res = []
            



def main():
    d = "23"
    solution =  Solution()
    print(solution.letterCombinations(d))