class Solution:
    def romanToInt(self, s: str) -> int:
        lookup = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000, 
            "IV": 4,
            "IX": 9,
            "XL":40,
            "XC": 90,
            "CD": 400,
            "CM": 900
        }
        length = len(s)
        idx = 0
        sum = 0
        while idx < length:
            if idx == length -1:
                sum += lookup.get(s[idx])
                idx += 1
            else:
                if (s[idx] == "I" and s[idx+1] in ["V", "X"]) or (s[idx] == "X" and s[idx+1] in ["L", "C"]) or (s[idx] == "C" and s[idx+1] in ["D", "M"]):
                    sum += lookup.get(s[idx:idx+2])
                    idx += 2
                else:
                    sum += lookup.get(s[idx])
                    idx += 1

        return sum



def main():
    s = "MCMXCIV"
    solution = Solution()
    print(solution.romanToInt(s))


main()