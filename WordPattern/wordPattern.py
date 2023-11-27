#Word Pattern Problem 
#time complexity - O(N) where N is the length of the string

def wordPattern(pattern, s):
    words = s.split()
    if len(words) != len(pattern):
        return False
    
    pattern_to_word = {}
    word_to_pattern = {}
    
    for char, word in zip(pattern, words):
        if char not in pattern_to_word:
            pattern_to_word[char] = word
        else:
            if pattern_to_word[char] != word:
                return False
        
        if word not in word_to_pattern:
            word_to_pattern[word] = char
        else:
            if word_to_pattern[word] != char:
                return False

        print(pattern_to_word)
        print(word_to_pattern)
    return True


if __name__ == "__main__":
    pattern = "aaaa"
    word = "jai jai"
    res = wordPattern(pattern, word)
    print(res)