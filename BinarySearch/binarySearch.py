#Binary Search Program
#time complexity - O(log n), where 'n' is the number of elements in the input array nums.

def binarySearch(nums, target):
    left = 0
    right = len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
            
    return -1
    

if __name__ == "__main__":
    nums= [-1, 0, 3, 5, 9, 12]
    target = 9
    res = binarySearch(nums, target)
    if res != -1:
        print("The target is found at index: ", res + 1)        #printing the index as i + 1 as indexing starts from 0 to n - 1
    else:
        print("Error, target doesn't exits in the given list: ", res)