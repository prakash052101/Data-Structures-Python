#Valid perfect square 
#time complexity - O(log n), where 'n' is the given number.

def isPerfectSquare(num):
    left, right = 1, num
    while left <= right:
        mid = left + (right - left) // 2
        square = mid * mid
        if square == num:
            return True
        elif square < num:
            left = mid + 1
        else:
            right = mid - 1
    return False

if __name__ == "__main__":
    num = 16
    print(isPerfectSquare(num))
    