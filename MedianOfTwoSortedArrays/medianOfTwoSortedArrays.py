#Median of Two Sorted Arrays Problem

#Method1 - by merging and sorting the arrays
#time complexity - O(N + M + n log n)

def findMedianSortedArraysM1(nums1, nums2) -> float:
    nums = []
    for num in nums1:
        nums.append(num)
    for num in nums2:
        nums.append(num)
    nums.sort()
    if len(nums) % 2 == 0:
        i = len(nums) // 2
        median = (nums[i - 1] + nums[i]) / 2
        return median
    else:
        i = len(nums) // 2
        median = nums[i]
        return median
    
#Method2 - By employing binary search method
#time complexity - O(log(min(M, N))) in the best-case scenario. 
# In scenarios where both arrays have similar lengths, the algorithm would effectively degrade to O(log(M + N)), 
# as the minimum of the two array lengths becomes a constant factor in the logarithmic complexity.

def findMedianSortedArraysM2(nums1, nums2) -> float:
    # Ensure nums1 is the smaller array or equal in size to nums2
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
        
    x, y = len(nums1), len(nums2)
    low, high = 0, x
    
    while low <= high:
        partitionX = (low + high) // 2        #calculating midpoint of array nums1
        partitionY = (x + y + 1) // 2 - partitionX  #calculating midpoint of array nums2 relative to nums1

        maxX = float("-inf") if partitionX == 0 else nums1[partitionX - 1] 
        minX = float("inf") if partitionX == x else nums1[partitionX]
        maxY = float("-inf") if partitionY == 0 else nums2[partitionY - 1]
        minY = float("inf") if partitionY == y else nums2[partitionY]

        if(maxX <= minY and maxY <= minX):
            if (x + y) % 2 == 0:
                return (max(maxX, maxY) + min(minX, minY)) / 2.0
            else:
                return (max(maxX, maxY))
        elif maxX > minY:
            high = partitionX - 1
        else:
            low = partitionX + 1           
        
        

if __name__ == "__main__":
    nums1 = [1, 3]
    nums2 = [2]
    print("Method M1", "Median", findMedianSortedArraysM1(nums1, nums2), sep = "::")
    print("Method M2", "Median", findMedianSortedArraysM2(nums1, nums2), sep = "::")