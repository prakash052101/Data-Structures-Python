#Isomorphic String
#time complexity - O(n), where n is the length of the input strings s and t.

def is_isomorphic(s, t):
    if len(s) != len(t):
        return False
    
    smapt = {}
    tmaps = {}
    
    for i in range(len(s)):
        charS = s[i]
        charT = t[i]
        
        if charS in smapt:
            if smapt[charS] != charT:
                return False
        else:
            smapt[charS] = charT
        
        if charT in tmaps:
            if tmaps[charT] != charS:
                return False
        else:
            tmaps[charT] = charS
    
    return True

if __name__ == "__main__":
    s1 = "egg"
    t1 = "add"
    print(is_isomorphic(s1, t1))  

    s2 = "foo"
    t2 = "bar"
    print(is_isomorphic(s2, t2)) 
