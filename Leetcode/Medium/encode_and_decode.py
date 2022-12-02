class Solution:
    def encode(self, s_list: list[str]) -> str:
        result: str = ""
        for s in s_list:
            result += f"{str(len(s))}#{s}"

        return result

    def decode(self, s: str) -> list[str]:
        res: list[str] = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1

            length = int(s[i:j])
            string = s[j + 1 : j + 1 + length]
            res.append(string)
            i = j + 1 + length
        return res


if __name__ == "__main__":
    a = ["hello", "#########world", "gg1#ngdown"]
    solution = Solution()
    encode_result = solution.encode(a)
    print(encode_result)
    print(solution.decode(encode_result) == a)
