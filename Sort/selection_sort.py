from typing import List

#  [9, 1, 18, 50, 3]

def selection_sort(array: List) -> None:
    length = len(array)

    #! switch 
    for i in range(length-1):  
        min = i
        for j in range(i+1, length):
            if array[j] < array[min]:
                min = j

        # Swap
        array[i], array[min] = array[min], array[i]


def main():
    unsorted_array = [9, 5, 1, 2, 3]
    selection_sort(unsorted_array)
    print(unsorted_array)

main()

        
