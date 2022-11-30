def bucket_sort(nums: list[int]) -> None:
    max_num = max(nums)
    min_num = min(nums)
    total_buckets = (max_num - min_num) + 1
    # Create an initialize counter array
    buckets: list[int] = [0] * total_buckets
    # num value minus min num is the index. Example: min_num = 1, num = 10, so the index 9 will count plus one.
    for num in nums:
        idx = num - min_num
        buckets[idx] += 1

    i = 0
    for j in range(len(buckets)):
        count = buckets[j]
        if count != 0:
            for _ in range(count):
                nums[i] = j + min_num
                i += 1


if __name__ == "__main__":
    nums = [1, 2, 3 , 10,  9 ,9, 6, 3 ,2, 0]
    bucket_sort(nums)
    print(nums)