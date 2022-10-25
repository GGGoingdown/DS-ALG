def fibo(num: int) -> int:
    if num in [0, 1]:
        return num

    p1 = 1
    p2 = 0
    for i in range(2, num+1):
        p1 = p1+p2
        print(f"N: {i} - Value: {p1}")
        p2 = p1-p2

    return p1


def main():
    n = 7

    print(fibo(n))

main()