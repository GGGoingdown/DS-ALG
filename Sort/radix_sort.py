def counting_sort(array: list[int], exp: int):
    n = len(array)

    output = [0]*n
    count = [0]*10
    
    for i in range(n):
        idx = array[i] // exp
        count[idx % 10] += 1

    for i in range(1, len(count)):
        count[i] += count[i-1]

    # Modify the output from back to front, because the idx get from count is large to small
    for i in range(n-1, -1, -1):
        idx = array[i] // exp
        output_index = count[idx%10]
        output[output_index-1] = array[i]
        count[idx%10] -= 1

    array[:] = output[:]


def radis_sort(array: list[int]):
    max1 = max(array)
    exp = 1

    while max1 / exp > 1:
        counting_sort(array, exp)
        exp *= 10



def main():
    array = [1001, 11, 1, 11111]

    radis_sort(array)
    print(array)

main()