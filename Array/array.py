def list_compare():
    li = [1, 2, 3, 4, 5]
    print(f"Before append: {li}")
    li.append(6) # O(1)
    print(f"After append: {li}")

    print(f"Before pop: {li}")
    print(li.pop()) # O(1)
    print(f"After pop: {li}")

    li.remove(1) # O(n)
    print(f"After remove: {li}")

    print(li.index(2)) # O(n)

    print(f"Before insert: {li}")
    li.insert(0, 6)   # O(n)
    print(f"After insert: {li}")


