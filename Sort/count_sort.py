def count_sort(array: list) -> None:
    max_element = int(max(array))
    min_element = int(min(array))
    print(f"Max - > {max_element}, Min -> {min_element}")

    range_of_elements = max_element - min_element + 1

    count_arr = [0]*range_of_elements
    output_arr = [0]*len(array)

    for i in range(0, len(array)):
        idx = array[i] - min_element
        count_arr[idx] += 1


    for i in range(1, len(count_arr)):
        count_arr[i] += count_arr[i-1]

    for i in range(len(array)-1, -1, -1):
        idx = count_arr[array[i] - min_element]
        output_arr[idx-1] = array[i]
        count_arr[idx] -= 1



def count_sort_with_positive_range(array: list) -> list:
    max_num = max(array)
    min_num = min(array)
    count_array = [0]* (max_num-min_num+1)
    output_array = [0] * len(array)

    for i in range(len(array)):  # Create counter table
        idx = array[i] - min_num
        count_array[idx] += 1

    # Each element at each index stores the sum of previous counts
    for i in range(1, len(count_array)):  
        count_array[i] += count_array[i-1]

    # Find the number of index
    for i in range(len(array)):
        idx = array[i] - min_num
        output_idx = count_array[idx]
        output_array[output_idx-1] = array[i]
        count_array[idx] -= 1

    return output_array



def main():
    # array = [-1, -9, 0, 10, 3]
    array = [10, 1, 7, 8, 3]
    print(count_sort_with_positive_range(array))



main()