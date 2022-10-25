from typing import Optional, List
from math import ceil

def left_child(i: int) -> int:
    return 2*i + 1

def right_child(i: int) -> int:
    return 2 * i + 2

def parent(i: int) -> int:
    if i == 0:
        return 0
    return ceil((i-2 )/ 2)

def is_leaf(array: List, index: int) -> bool:
    n = len(array)
    if left_child(index) >= n and right_child(index) >= n:
        return True
    return False


def fix_down(array: List, index:int) -> None:
    n = index
    while not is_leaf(array, n):
        j = left_child(n)
        if j != len(array)-1 and array[j] < array[j+1]:
            j += 1
        if array[n] > array[j]:
            break
        # Swap 
        array[j], array[n] = array[n], array[j]
        n = j


def heapify(array: List):
    n = len(array)
    for i in range(parent(n-1), -1, -1):
        fix_down(array, i)

def heap_sort(array: List):
    heapify(array)

    print(f"Heapify array - {array}")
    n = len(array)-1
    while n > 0:
        array[0], array[n] = array[n], array[0]
        new_array = array[:n]
        fix_down(new_array, 0)
        array[:n] = new_array
        n -= 1



def main():
    array  = [30, 1, 31, 50, 9]
    heap_sort(array)
    print(array)

main()