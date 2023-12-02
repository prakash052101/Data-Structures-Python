#Remove Duplicates
#time complexity - O(n) where n is the length of the input array.

def removeDuplicates(nums) -> int:
    # Check for edge case where nums is empty
    if not nums:
        return 0

    # Initialize a pointer for unique elements
    unique = 1
    
    # Iterate through the array starting from the second element
    for i in range(1, len(nums)):
        if nums[i] != nums[i-1]:
            nums[unique] = nums[i]
            unique += 1             #Move the unique index forward
            
    return unique

if __name__ == "__main__":
    nums1 = [1,1,2]
    nums2 = [0,0,1,1,1,2,2,3,3,4]
    print(removeDuplicates(nums1), removeDuplicates(nums2), sep="\n")