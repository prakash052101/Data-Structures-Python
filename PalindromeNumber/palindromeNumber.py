#Palindrome Number
#time complexity - O(log10(num)), where num is the given integer

def isPalindrome(num) -> bool:
        # Handling negative numbers or numbers ending with 0 (excluding 0 itself)
        if num < 0 or (num % 10 == 0 and num != 0):
            return False

        reverse = 0
        while num > reverse:
            reverse = reverse * 10 + num % 10
            num //= 10

        # For even-length numbers: x == reverse
        # For odd-length numbers: x == reverse // 10 (ex: 12321 => x=12, reverse=123)
        return num == reverse or num == reverse // 10


if __name__ == "__main__":
    num = 10
    num1 = 11
    num2 = 18
    num3 = 121
    print(isPalindrome(num), isPalindrome(num1), isPalindrome(num2), isPalindrome(num3), sep="::")