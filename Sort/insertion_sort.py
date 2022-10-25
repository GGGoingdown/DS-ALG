def fix_down(array: list[int], index: int) -> None:
    for i in range(index, 0, -1):
        if array[i] < array[i-1]:
            array[i], array[i-1] = array[i-1], array[i]
        else:
            break

def insertion_sort(array: list[int]) -> None:
    length = len(array)
    for i in range(length-1):
        if array[i+1] < array[i]:
            fix_down(array, i+1)


def main():
    array = [10, 1, 9, 8, 50, 4, 3]
    insertion_sort(array)
    print(array)



main()