#leetcode longest palindrome substring problem in python

#time complexity -  due to the nested nature of the loop and the 
#expanding process around each center, the time complexity of this 
#solution is quadratic, making it O(n^2) in the worst-case scenario

def longestPalindromeSubstring(s:str) -> str:
    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]
    
    longest = ""
    for i in range(len(s)):
        #if the palindrome is odd
        Palindrome_Odd = expand_around_center(i, i)
        if len(Palindrome_Odd) > len(longest):
            longest = Palindrome_Odd

        #if Palidrome is even
        Palindrome_Even = expand_around_center(i, i + 1)
        if len(Palindrome_Even) > len(longest):
            longest = Palindrome_Even

    return longest

if __name__ == "__main__":
    string = "wklelkd"
    print(longestPalindromeSubstring(string))