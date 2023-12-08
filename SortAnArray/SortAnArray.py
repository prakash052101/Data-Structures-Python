#Sort an Array

#Method 1 - Merge Sort
#time complexity - O(nlogn)
def sortArrayM1(nums):
    def Merge(A, lb, mid, ub):
        i = lb
        j = mid + 1
        k = lb
        B = [0] * (ub + 1)
        while i <= mid and j <= ub:
            if A[i] <= A[j]:
                B[k] = A[i]
                i += 1
                    
            else:
                B[k] = A[j]
                j += 1
                    
            k += 1
                
        if i > mid:
            while j <= ub:
                B[k] = A[j] 
                k += 1
                j += 1
        else:
            while i <= mid:
                B[k] = A[i]
                k += 1
                i += 1
                    
        for k in range(lb, ub + 1):
            A[k] = B[k]         


    def MergeSort(A, lb, ub):
        if lb < ub:
            mid = (lb + ub) // 2
            MergeSort(A, lb, mid)
            MergeSort(A, mid+1, ub)
            Merge(A, lb, mid, ub)
            
    MergeSort(nums, 0, len(nums) - 1)
    return nums
        

#Method 2 - Bottom up Merge Sort
#time complexity - O(nlogn)
def sortArrayM2(nums):
    def merge(left, right):
        merged = []
        while left and right:
            if left[0] <= right[0]:
                merged.append(left.pop(0))
            else:
                merged.append(right.pop(0))
        merged.extend(left or right)
        return merged

    n = len(nums)
    size = 1
    while size < n:
        for i in range(0, n - size, size * 2):
            left = nums[i:i + size]
            right = nums[i + size:i + size * 2]
            nums[i:i + size * 2] = merge(left, right)
        size *= 2
    return nums



if __name__ =="__main__":
    nums1 = [5, 2, 3, 1]
    nums2 = [5,1,1,2,0,0]
    print(sortArrayM1(nums1))
    print(sortArrayM2(nums2))