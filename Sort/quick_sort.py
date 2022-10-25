from typing import List

def quick_sort_range(array: List, first: int, last: int) -> None:
    if first >= last:
        return None

    pivot = array[first]
    pos = last

    for i in range(last, first, -1):
        """ 
        If value greater than pivot,
        swap pos and index to make sure the value of index greater than pos are bigger than pivot 
        """
        if array[i] > pivot: 
            array[i], array[pos] = array[pos], array[i]
            pos -= 1

    # Swap pivot and pos
    array[first], array[pos] = array[pos], array[first]
    # Divided and conquer
    quick_sort_range(array, first, pos-1)  # Left side
    quick_sort_range(array, pos+1, last) # Right side


def quick_sort(array: List) -> None:
    length = len(array)
    first_index = 0
    last_index = length - 1
    quick_sort_range(array, first_index, last_index)


def main() -> None:
    a = [3, 1, 2, 9, 7]
    quick_sort(a)

    print(a)


main()