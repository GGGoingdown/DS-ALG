
def reverse(string: str) -> str:
    if not isinstance(string, str):
        raise Exception(f"Invalid type: {type(string)}")
    
    total = len(string)
    if total == 0:
        return ""

    reverse_string = []
    total = len(string)
    for i in range(total-1, 0, -1):
        reverse_string.append(string[i])
    reverse_string.append(string[0])

    return "".join(reverse_string)


def reverse2(string: str) -> str:
    return string[::-1]


def main():
    a = "abc"

    reverse_a = reverse2(a)

    print(reverse_a)

if __name__ == "__main__":
    main()