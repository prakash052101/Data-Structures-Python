def removeAlmostEqualCharacters(word) -> int:
    if len(word) < 2:
        return 0
    count = 0
    i = 1
    while i < len(word):
        if (ord(word[i]) - 1) == ord(word[i - 1]):
            count += 1
            i += 2
        elif (ord(word[i - 1]) - 1) == ord(word[i]):
            count += 1
            i += 2
        elif word[i] == word[i - 1]:
            count += 1
            i += 2
        else:
            i += 1
    return count

if __name__ =="__main__":
    word1 = "aaaaa"
    word2 = "abddez"
    print(removeAlmostEqualCharacters(word1))
    print(removeAlmostEqualCharacters(word2))
    
    