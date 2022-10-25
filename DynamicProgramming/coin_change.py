from typing import List

def coin_change(coins: List[int], amount: int):
    lookup_table_length = amount +1
    lookup_table = [amount+1]*lookup_table_length
    lookup_table[0] = 0

    for i in range(1, lookup_table_length):
        for coin in coins:
            if coin <= i:
                lookup_table[i] = min(lookup_table[i], lookup_table[i-coin] + 1)

    if lookup_table[amount] > amount:
        return -1

    for index, num in enumerate(lookup_table):
        print(f"Index: {index} - Num: {num}")
    return lookup_table[amount]


def main():
    print(coin_change([1, 15, 20], 45))




main()