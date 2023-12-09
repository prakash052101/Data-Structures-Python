def findIntersectionValues(nums1, nums2):
    set1 = set(nums1)
    set2 = set(nums2)

    count1 = sum(1 for num in nums1 if num in set2)
    count2 = sum(1 for num in nums2 if num in set1)

    return [count1, count2]

if __name__ == "__main__":
    nums1 = [4,3,2,3,1]
    nums2 = [2,2,5,2,3,6]
    print(findIntersectionValues(nums1, nums2))