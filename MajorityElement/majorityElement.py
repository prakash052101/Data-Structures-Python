#Majority Element - Boyer-Moore Voting Algorithm 
#time complexity - O(n), where n is the length of the input array

def majorityElement(nums) -> int:
    count = 0
    el = None
    
    for i in range(len(nums)):
        if count == 0:
            el = nums[i]
            count = 1
        elif el == nums[i]:
            count += 1
        else:
            count -= 1
    
    # Verify if the assumed majority element occurs more than n/2 times
    count = 0
    for i in range(len(nums)):
        if nums[i] == el:
            count += 1

    if count > len(nums) / 2:
        return el
    
    return -1  # If no majority element found
    
if __name__ == "__main__":
    nums1 = [3,2,3]
    nums2 = [2,2,1,1,1,2,2]
    print(majorityElement(nums1), majorityElement(nums2), sep="::")