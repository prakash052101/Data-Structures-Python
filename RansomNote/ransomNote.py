#Ransom Note
#time complexity - O(m + n)
# m: Length of ransomNote
# n: Length of magazine


from collections import defaultdict
def canConstruct(ransomNote, magazine) -> bool:
    count = defaultdict(int)

    for char in magazine:
        count[char] += 1

    for char in ransomNote:
        if count[char] > 0:
            count[char] -= 1
        else:
            return False

    return True

if __name__ == "__main__":
    ransomNote = "aa"
    magazine = "aab"
    print(canConstruct(ransomNote, magazine))
    

