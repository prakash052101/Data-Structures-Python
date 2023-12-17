#Divide Array Into Arrays with Max Difference
#time complexity - O(N log N) time, where N is the number of elements in nums.

def divideArray(nums, k):
    nums.sort()
    result = []

    for i in range(len(nums) // 3):
        if nums[3 * i + 2] - nums[3 * i] > k:
            return []
        result.append([nums[3 * i], nums[3 * i + 1], nums[3 * i + 2]])

    return result

if __name__ == "__main__":
    nums = [1,3,4,8,7,9,3,5,1]
    k = 2
    print(divideArray(nums, k))
    