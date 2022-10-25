def fibonacciRecursive(n: int) -> int:
    # print(f"Inner fibonacci - {n}")
    if n <= 1:
        return n 
    
    return fibonacciRecursive(n-1) + fibonacciRecursive(n-2)


def fibonacciIterative(n: int) -> int:
    if n <=1:
        return n

    start_num = 1
    return_num = 1
    for _ in range(2, n):
        temp = return_num + start_num
        start_num = return_num
        return_num = temp

    return return_num


def main():
    num = 40
    # r_result = fibonacciRecursive(num) 
    i_result = fibonacciIterative(num)
    # assert r_result == i_result, f"Recursive: {r_result} - Iterative: {i_result}"
    print(i_result)

main()