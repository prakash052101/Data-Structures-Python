#power of Two Problem


#Method -1 (without using loops or recursion)

#For a positive integer n to be a power of two, it must satisfy two conditions:
#1) n should be greater than 0.
#2) The binary representation of n should have only one bit set to 1.

def isPowerOfTwo(n) -> bool:
        return n > 0 and (n & (n - 1)) == 0
    
if __name__ == "__main__":
    num = 16
    result = isPowerOfTwo(num)
    print(f"{num} is a power of two: {result}")