#reverse of an integer

#method 1
#Time Complexity: O(log10(n))
#Operations: Involves converting the integer to a string, reversing the string using slicing ([::-1]), 
#and converting it back to an integer.

def reverseIntegerM1(num):
    sign = -1 if num < 1 else 1
    x = abs(num)
    str1 = str(x)
    reversed = int(str1[::-1])
    reversed_num = sign * reversed
    
    if reversed_num < -2**31 or reversed_num > 2**31 - 1:
            return 0
        
    return reversed_num


#method2
#time complexity -  O(log10(n))
#Operations: Involves arithmetic operations (modulus, division, multiplication) within a loop to reverse digits directly.
def reverseIntegerM2(x):
    sign = -1 if x < 0 else 1
    x = abs(x)
    reversed_num = 0
    
    while x != 0:
        digit = x % 10
        reversed_num = reversed_num * 10 + digit
        x //= 10
    
    reversed_num *= sign
    
    if reversed_num < -2**31 or reversed_num > 2**31 - 1:
        return 0
    
    return reversed_num

if __name__ == "__main__":  
    print(reverseIntegerM1(123456789))
    print(reverseIntegerM2(-123456789))