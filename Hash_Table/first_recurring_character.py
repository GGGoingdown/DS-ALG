from typing import List, Optional, Dict

def first_recurring_character(array: List[int]) -> Optional[int]:
    lookup: Dict[int, int] = {}
    for c in array:
        if lookup.get(c) is None:
            lookup[c] = 1
        else:
            return c

    return None


def main():
    array = [1, 1, 3, 5, 7]
    print(first_recurring_character(array))

main()