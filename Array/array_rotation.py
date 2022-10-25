def reversal(array: list[int], start: int, end: int) -> None:
    while start < end:
        temp = array[start]
        array[start] = array[end]
        array[end] = temp
        start += 1
        end -= 1


def rotation(array: list[int], d: int) -> None:
    n = len(array)
    d = d % n   # Get the remainder
    reversal(array, 0, d-1) # [2, 1, 3, 4, 5, 6]
    reversal(array, d, n-1) # [2, 1, 6, 5, 4, 3]
    reversal(array, 0, n-1) # [3, 4, 5, 6, 1, 2]


def main():
    ar = [1,2,3,4,5,6]
    rotation(ar, 2)
    print(ar)

main()