#leetcode problem longest substring without repeatition
#time complexity - O(n)


def lengthOfLongestSubstring(s: str) -> int:
    chars_indices = {}
    max_length = 0
    start = 0

    for end in range(len(s)):
        if s[end] in chars_indices:
            start = max(start, chars_indices[s[end]]+1)
        
        chars_indices[s[end]] = end
        max_length = max(max_length, end - start + 1)

    return max_length

if __name__ == "__main__":
    result = lengthOfLongestSubstring("abcdbce")
    print(result)

