class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lookup = {}
        max_str = 0
        window_start = 0
        window_end = 0
        while window_end < len(s):
            current_s = s[window_end]
            if lookup.get(current_s):
                max_str = max(max_str, window_end - window_start)
                while window_start < window_end:
                    del lookup[s[window_start]]
                    if s[window_start] == current_s:
                        window_start += 1
                        break

                    window_start += 1

            lookup[current_s] = 1
            window_end += 1
        
        return max(max_str, window_end - window_start)



def main():
    string = " "
    # string = "pwwkew"
    solution = Solution()
    print(solution.lengthOfLongestSubstring(string))



main()