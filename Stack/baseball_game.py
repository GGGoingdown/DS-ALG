""" 
Input: ops = ["5","2","C","D","+"]
Output: 30
Explanation:
"5" - Add 5 to the record, record is now [5].
"2" - Add 2 to the record, record is now [5, 2].
"C" - Invalidate and remove the previous score, record is now [5].
"D" - Add 2 * 5 = 10 to the record, record is now [5, 10].
"+" - Add 5 + 10 = 15 to the record, record is now [5, 10, 15].
The total sum is 5 + 10 + 15 = 30.

---

Input: ops = ["1","C"]
Output: 0
Explanation:
"1" - Add 1 to the record, record is now [1].
"C" - Invalidate and remove the previous score, record is now [].
Since the record is empty, the total sum is 0.


"""


class Solution:
    def calPoints(self, operations: list[str]) -> int:
        new_records: list[int] = []
        for v in operations:
            if v == "C":
                new_records.pop()
                continue
            
            if v == "D":
                last_val = new_records[-1]
                append_val = int(last_val) * 2
                new_records.append(append_val)
                continue
                
            if v == "+": 
                last_one_val, last_two_val = new_records[-1], new_records[-2]
                append_val = int(last_one_val) + int(last_two_val)
                new_records.append(append_val)
                continue
            # Others
            new_records.append(int(v))
        
        return sum(new_records)





if __name__ == "__main__":
    from utils import ResultValidator

    v1 = ResultValidator(inputs=["5","2","C","D","+"], expected_result=30)
    v2 = ResultValidator(inputs=["5","-2","4","C","D","9","+","+"], expected_result=27)
    v3 = ResultValidator(inputs=["1","C"], expected_result=0)
    solution  = Solution()
    for v in [v1, v2, v3]:
        result = solution.calPoints(v.inputs)
        v.validate(result)

