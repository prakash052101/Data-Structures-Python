#Merge Sorted Array Problem
#time complexity - O(m + n), where m is the number of elements in nums1,
#and n is the number of elements in nums2

def mergeSortedArray(nums1, m, nums2, n):
    i = m - 1
    j = n - 1
    k = m + n - 1
    
    while i >= 0 and j >= 0:
        
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
            
        else:
            nums1[k] = nums2[j]
            j -= 1
            
        k -= 1
    
    
    # If there are remaining elements in nums2, copy them directly to nums1
    while j >= 0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1
        
    print("Merge Sorted Array Result::", nums1)
    
    
if __name__ == "__main__":
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    mergeSortedArray(nums1, m, nums2, n)