#Rotate an Array

#Method1 - using reversal
#time complexity - O(n), where 'n' is the number of elements in the nums array.

def rotateM1(nums, k) -> None:
    n = len(nums)
    k = k % n

    def reverse(arr, start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1

    reverse(nums, 0, n - 1)  # Reverse the entire array
    reverse(nums, 0, k - 1)  # Reverse the first k elements
    reverse(nums, k, n - 1)  # Reverse the remaining elements


#Method2 - using additional array
#time complexity - O(n), where 'n' is the number of elements in the nums array.

def rotateM2(nums, k) -> None:
    n = len(nums)
    k = k % n
    if k == 0:
        return nums

    rotated = [0] * n
    for i in range(n):
        rotated[(i + k) % n] = nums[i]

    nums[:] = rotated     
    

if __name__ == "__main__":
    nums1 = [1, 2, 3, 4, 5, 6, 7]
    k1 = 3
    nums2 = [-1, -100, 3, 99]
    k2 = 2
    rotateM1(nums1, k1)
    print(nums1)
    rotateM2(nums2, k2)
    print(nums2)