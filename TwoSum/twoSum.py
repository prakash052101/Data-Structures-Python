#leetcode twoSum problem solution in python
#time complexity O(n)

def twoSum(nums, target):
    nums_indices = {}   #initialize an empty dictionary to store number and its index

    for i, num in enumerate(nums):
        complement = target - num 
        if complement in nums_indices:
            return [nums_indices[complement], i]    # Return the indices of the two numbers
        
        nums_indices[num] = i        # Store the number and its index in the dictionary
     # If no solution is found
    return None

if __name__ == "__main__":
    nums = [4, 10, 6, 7, 8]
    target = 11
    result = twoSum(nums, target)
    print(result)