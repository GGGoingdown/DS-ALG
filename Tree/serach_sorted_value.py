from typing import List

def binary_search(array: List[int], value: int):
    length = len(array)
    l = 0
    r = length - 1
    while l <= r:
        print(f"{l} - {r}")
        mid = l + int((r-l) / 2)
        if value == array[mid]:
            return mid
        elif value < array[mid]:
            r = mid - 1
        else:
            l = mid + 1
    return -1


def main():
    sorted_list = [1, 3, 5, 7]
    print(binary_search(sorted_list, 8))

main()