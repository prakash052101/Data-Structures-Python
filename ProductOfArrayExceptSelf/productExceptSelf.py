#Product of Array Except Self
#time complexity - O(n)

def productExceptSelf(nums):
    n = len(nums)
    left = [1] * n
    right = [1] * n
    result = [1] * n

    # Calculate left products
    for i in range(1, n):
        left[i] = left[i - 1] * nums[i - 1]

    # Calculate right products
    for i in range(n - 2, -1, -1):
        right[i] = right[i + 1] * nums[i + 1]

    # Multiply left and right products to get the result
    for i in range(n):
        result[i] = left[i] * right[i]

    return result

if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    print(productExceptSelf(nums))
    
    nums =  [-1, 1, 0, -3, 3]
    print(productExceptSelf(nums))