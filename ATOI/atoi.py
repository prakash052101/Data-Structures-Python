#String to Integer Problem

#Method1 - using lstrip and isDigit
#time complexity - O(n) where n is the length of the input string s
def atoiM1(s):
    s = s.strip()  # Remove leading and trailing whitespace
    if not s:
        return 0
    
    sign = 1
    result = 0
    i = 0
    
    if s[0] in ['+', '-']:  # Handle sign
        if s[0] == '-':
            sign = -1
        i = 1
    
    while i < len(s) and s[i].isdigit():  # Convert digits to integer
        result = result * 10 + int(s[i])
        i += 1
    
    return max(-2**31, min(sign * result, 2**31 - 1))  # Limit the result to 32-bit signed integer range



#Method2 - using loops
#time complexity - O(n) where n is the length of the input string s
def atoiM2(s):
    # Remove leading whitespace
    while s and s[0] == ' ':
        s = s[1:]

    if not s:
        return 0
    
    sign = 1
    result = 0
    i = 0
    
    if s[0] == '-':  # Handle negative sign
        sign = -1
        i = 1
    elif s[0] == '+':  # Handle positive sign
        i = 1
    
    # Convert digits to integer
    while i < len(s) and '0' <= s[i] <= '9':
        result = result * 10 + ord(s[i]) - ord('0')
        i += 1
    
    return max(-2**31, min(sign * result, 2**31 - 1))  # Limit the result to 32-bit signed integer range


#Method3 - using regex
#time complexity - O(n), where n is the length of the input string.

import re

def atoiM3(s):
    pattern = re.compile(r'^\s*([+-]?\d+)')
    match = pattern.match(s)
    
    if match:
        result = int(match.group(1))
        return max(-2**31, min(result, 2**31 - 1))
    else:
        return 0



if __name__ == "__main__":
    s1 = "4193 with words"
    s2 = "   -42"
    s3 = "42"
    print("Method 1 Output: ", atoiM1(s1))
    print("Method 2 Output: ", atoiM2(s2))
    print("Method 3 Output: ", atoiM3(s3))
