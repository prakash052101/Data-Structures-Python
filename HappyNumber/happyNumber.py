#Happy Number
#time complexity - O(log n * d), where log n represents the number of iterations needed in the 
#worst case for n to reach 1 (which is bounded by the number of digits in n), 
#and d represents the number of digits in n.

def isHappy(n):
    def getNext(n):
        total = 0
        while n > 0:
            n, digit = divmod(n, 10)
            total += digit ** 2
        return total

    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = getNext(n)

    return n == 1

if __name__ == "__main__":
    n = 19
    print(isHappy(n))