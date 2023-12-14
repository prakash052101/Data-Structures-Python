#First Unique character in a String
#time complexity - the overall time complexity of the code is O(n + n), 
#which simplifies to O(n), where 'n' is the length of the string s.
def firstUniqChar(s: str) -> int:
    tracker = {}
    for char in s:
        if char in tracker:
            tracker[char] += 1
        else:
            tracker[char] = 1
        
    for index, char in enumerate(s):
        if tracker[char] == 1:
            return index
                

    return -1

if __name__ == "__main__":
    s = "loveleetcode"
    print(firstUniqChar(s))