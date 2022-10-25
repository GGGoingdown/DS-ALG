from typing import List

        
def merge_sort(array: List):
    if len(array) > 1:
        mid = len(array) // 2
        left_array = array[:mid]
        right_array = array[mid:]
        merge_sort(left_array)
        merge_sort(right_array)

        print(f"Left array -> {left_array}")
        print(f"Right array -> {right_array}")
        print(array)
        print("*"*50)

        head_l, head_r, index = 0, 0, 0
        while head_l < len(left_array) and head_r < len(right_array):
            if left_array[head_l] < right_array[head_r]:
                array[index] = left_array[head_l]
                head_l += 1
            else:
                array[index] = right_array[head_r]
                head_r += 1

            index += 1

        while head_l < len(left_array):
            array[index] = left_array[head_l]
            head_l += 1
            index += 1

        while head_r < len(right_array):
            array[index] = right_array[head_r]
            head_r += 1
            index += 1
        


    else: # Base case. Example -> [1]
        return array


def main():
    array = [10, 1, 7, 3, 30, 4]
    merge_sort(array)
    print(array)



main()