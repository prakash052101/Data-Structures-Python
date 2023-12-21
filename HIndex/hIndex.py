#H Index


#Method1
#time complexity - O(n log n)
def hIndexM1(citations):
    citations.sort(reverse=True)
    h = 0

    for i, citation in enumerate(citations, start=1):
        if citation >= i:
            h = i
        else:
            break

    return h

#Method2
#time complexity - O(n), where n is the length of the input array citations.

def hIndexM2(citations):
    n = len(citations)
    counter = [0] * (n + 1)  # Initialize a count array of size n+1

    # Count the occurrences of each citation
    for citation in citations:
        if citation >= n:
            counter[n] += 1
        else:
            counter[citation] += 1

    total = 0

    # Iterate through the count array to find the h-index
    for i in range(n, -1, -1):
        total += counter[i]
        if total >= i:
            return i

    return 0




if __name__ == "__main__":
    citations1 = [3, 0, 6, 1, 5]
    print(hIndexM1(citations1)) 

    citations2 = [1, 3, 1]
    print(hIndexM2(citations2)) 