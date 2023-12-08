#Sort colors

#Method 1: Insertion Sort
#this one uses O(n^2) time complexity
def sortColorsM1(nums):
    for i in range(1, len(nums)):
        temp = nums[i]
        j = i - 1
        while(j >= 0 and nums[j] > temp):
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = temp
 

#Method 2 -Binary Insertion Sort -  this method uses the binary search or divide and conquer method to find
#the appropriate place to insert the element instead of pairwise swap
#the time complexity of this method is O(nlog(n)) comparisons and O(n^2) swaps
def sortColorsM2(nums):
    for i in range(1, len(nums)):
        key = nums[i]

        # Binary search to find the correct position of key in the sorted sub-array
        left, right = 0, i - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > key:
              right = mid - 1
            else:
              left = mid + 1
          
            # Shift elements to make space for key
        for j in range(i - 1, left - 1, -1):
            nums[j + 1] = nums[j]
          
          # Place key in its correct position
        nums[left] = key   


if __name__ == "__main__":
    nums1 = [2, 0, 2, 1, 1, 0]
    nums2 = [2, 1, 0]
    sortColorsM1(nums1)
    sortColorsM2(nums2)
    print(nums1)
    print(nums2)
    
