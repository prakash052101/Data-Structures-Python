#Find Square-Root Problem
#time complexity - O(log N), where N is the value of the given non-negative integer x.

def findSqrt(x):
    if x == 0 or x == 1:
        return x
    
    left, right = 1, x // 2
    
    while left <= right:
        mid = left + (right - left) // 2
        square = mid * mid
        
        if square == x:
            return mid
        elif square < x:
            left = mid + 1
        else:
            right = mid - 1
            
    return right  # Returning right instead of -1 to get the floor value


if __name__ == "__main__":
    num = 1024
    result = findSqrt(num)
    print(f"The square root of {num} is {result}")
