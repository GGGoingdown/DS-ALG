""" 
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example :
Input: s = "anagram", t = "nagaram"
Output: true

Input: s = "rat", t = "car"
Output: false
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        apl_dic: dict[str, int] = {}
        for s_ in s:
            exist_val = apl_dic.get(s_)
            if exist_val:
                apl_dic[s_] = exist_val + 1
                continue

            apl_dic[s_] = 1

        for t_ in t:
            exist_val = apl_dic.get(t_)
            if not exist_val:
                return False

            apl_dic[t_] = exist_val - 1

        return True


if __name__ == "__main__":
    s1, t1 = "anagram", "nagaram"
    solution = Solution()
    result = solution.isAnagram(s1, t1)
    print(result)
