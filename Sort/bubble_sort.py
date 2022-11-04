def bubble_sort(array: list[int]) -> None:
    count = len(array) - 1
    while count:
        for i in range(count):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]

        count -= 1


def main():
    array = [100, 8, 200, 1, 0, 20]
    bubble_sort(array)
    print(array)


main()
