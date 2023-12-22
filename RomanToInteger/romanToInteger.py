#Roman To Integer
#time complexity - O(n), where n is the length of the input string s.

def romanToInt(s):
    roman = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    total = 0
    prev = 0

    for char in s:
        current = roman[char]
        total += current

        if prev < current:
            total -= 2 * prev

        prev = current

    return total

if __name__ == "__main__":
    s1 = "III"
    print(romanToInt(s1)) 

    s2 = "LVIII"
    print(romanToInt(s2))  

    s3 = "MCMXCIV"
    print(romanToInt(s3))
