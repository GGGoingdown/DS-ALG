def find_factorial_recursive(num: int):
    if num == 1:
        return 1
    return num * find_factorial_recursive(num-1)

def find_factorial_iterative(num: int):
    total = 1
    for i in range(1, num+1):
        total *= i

    return total


def main():
    num = 10
    recursive_result = find_factorial_recursive(num)
    iterative_result = find_factorial_iterative(num)

    print(recursive_result, iterative_result)


main()