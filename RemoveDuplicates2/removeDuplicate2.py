#Remove Duplicates - II
#time complexity - O(N) where, n is the number of elements in the nums list.
def removeDuplicates(nums) -> int:
    if len(nums) <= 2:
        return len(nums)
    j = 1  
    for i in range(2, len(nums)):
        if nums[i] != nums[j - 1]:
            j += 1
            nums[j] = nums[i]

    return j + 1 

if __name__ == "__main__":
    nums1 = [1,1,1,2,2,3]
    print(removeDuplicates(nums1))
    
    nums2 = [0,0,1,1,1,1,2,3,3]
    print(removeDuplicates(nums2))