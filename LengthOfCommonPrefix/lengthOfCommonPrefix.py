#length of common prefix
#Method-1 Brute force
#time complexity - O(n*m)
def longestCommonPrefixM1(strs) -> str:
    if not strs:
       return ""

    prefix = strs[0]
    for string in strs[1:]:
        while string.find(prefix) != 0:
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix


#Method-2 Using sort()
#time complexity - O(n*m*logm)
def longestCommonPrefixM2(strs):
    if not strs:
        return ""

    # Sort the array of strings to bring the strings with the common prefix together
    strs.sort()

    # Consider the first and last string after sorting
    first = strs[0]
    last = strs[-1]
    length = min(len(first), len(last))

    # Find the common prefix between the first and last strings
    i = 0
    while i < length and first[i] == last[i]:
        i += 1

    return first[:i]



if __name__ == "__main__":
    
    input1 = ["flower", "flow", "flight"]
    input2 = ["dog", "racecar", "car"]

    print(longestCommonPrefixM1(input1)) 
    print(longestCommonPrefixM2(input2))  



