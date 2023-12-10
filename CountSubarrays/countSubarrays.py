# Count Subarrays Where Max Element Appears at Least K Times
#time complexity -  O(n), where n is the length of the nums list.

def countSubarrays(nums, k) -> int:
    n = len(nums)
    count = 0
    max_num = max(nums)
    start = 0
    max_count = 0

    for end in range(n):
        if nums[end] == max_num:
            max_count += 1

        while start < n and max_count >= k:
            count += n - end
            if nums[start] == max_num:
                max_count -= 1
            start += 1

    return count

if __name__ == "__main__":
    nums = [1,3,2,3,3]
    k = 2
    print(countSubarrays(nums, k))