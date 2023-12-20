#Conatin Duplicates
#time complexity - O(n)

def containsNearbyDuplicate(nums, k):
    numIndices = {}

    for i, num in enumerate(nums):
        if num in numIndices and abs(i - numIndices[num]) <= k:
            return True
        numIndices[num] = i

    return False

if __name__ == "__main__":
    nums = [1,0,1,1]
    k = 1
    print(containsNearbyDuplicate(nums, k))
    
    nums = [1,2,3,1,2,3]
    k = 2
    print(containsNearbyDuplicate(nums, k))
    
    nums = [1,2,3,1]
    k = 3
    print(containsNearbyDuplicate(nums, k))