from typing import List
""" 
a1 = [1, 2, 3]
a2 = [4, 5, 6]

"""

def merge_array(a1: List, a2: List) -> List:
    a1_len = len(a1)
    a2_len = len(a2)
    if a1_len == 0:
        return a2
    if a2_len == 0:
        return a1

    a1_index = 0
    a2_index = 0
    return_array = []

    while a1_index < a1_len or a2_index < a2_len:
        if a1_index >= a1_len:
            return_array.append(a2[a2_index])
            a2_index += 1
            continue
        
        if a2_index >= a2_len:
            return_array.append(a1[a1_index])
            a1_index += 1            
            continue

        if a1[a1_index] <= a2[a2_index]:
            return_array.append(a1[a1_index])
            a1_index += 1
        else:
            return_array.append(a2[a2_index])
            a2_index += 1


    return return_array


def main():
    a1 = []
    a2 = []

    print(merge_array(a1, a2))



if __name__ == "__main__":
    main()