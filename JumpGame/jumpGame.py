#Jump Game
#time compexity - O(n), where n is the length of the input array nums.

def canJump(nums):
    j = 0  # Initialize the maximum reachable index

    for i in range(len(nums)):
        # If the current index is beyond the maximum reachable index, return False
        if i > j:
            return False
        
        # Update the maximum reachable index
        j = max(j, i + nums[i])

        # If the maximum reachable index reaches or surpasses the last index, return True
        if j >= len(nums) - 1:
            return True

    return False

if __name__ == "__main__":
    nums1 = [2, 3, 1, 1, 4]
    print(canJump(nums1))  

    nums2 = [3, 2, 1, 0, 4]
    print(canJump(nums2))  
