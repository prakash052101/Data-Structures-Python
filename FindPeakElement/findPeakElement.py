#Find Peak Element
#time complexity - O(log n), where n is the number of elements in the nums list
#Divide and conquer strategy
def findPeakElement(nums) -> int:
    if not nums:
        return -1
        
    i = 0
    j = len(nums) - 1
    while i < j:
        mid = (i + j) // 2
        if nums[mid] < nums[mid + 1]:
            i += 1
        else:
            j = mid

    return i

if __name__ == "__main__":
    nums = [1,2,3,1]
    print(findPeakElement(nums))