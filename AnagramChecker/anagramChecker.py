#Anagram Checker problem
#time comlexity - O(n)

def anagramChecker(str1, str2):
    if len(str1) != len(str2):
        return False
    
    chars_freq = {}
    for char in str1:
        if char in chars_freq:
            chars_freq[char] += 1
        else:
            chars_freq[char] = 1

    for char in str2:
        if char in chars_freq:
            chars_freq[char] -= 1

        else:
            return False
        
    return all(value == 0 for value in chars_freq.values())

if __name__ == "__main__":
    str1 = "listen"
    str2 = "silent"
    print(anagramChecker(str1, str2))
        


