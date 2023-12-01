#Remove Element Problem
#time complexity - O(n)

def removeElement(nums, val):
    # Use two pointers - one for iterating and one for overwriting non-val elements
    # Move non-val elements to the beginning of the list
    i = 0
    for j in range(len(nums)):
        if nums[j] != val:
            nums[i] = nums[j]
            i += 1
    
    # Remove the extra elements (if any) at the end of the list
    nums = nums[:i]
    
    return nums, i  # Return the modified list and its length


if __name__ == "__main__":
    nums = [0,1,2,2,3,0,4,2]
    val = 2

    nums, k = removeElement(nums, val)
    print(k, nums, sep="::")