#Find Missing and Repeated Values
#time complexity - O(N), where N is the the total number of elements in the grid.

def findMissingAndRepeatedValues(grid):
    nums = set()
    repeated = 0
    start = 0
    n = 0

    for row in grid:
        for num in row:
            n += 1
            if num in nums:
                repeated = num
            else:
                nums.add(num)
            start += num
                
    total = n * (n + 1) // 2
    missing = repeated + total - start

    return [repeated, missing]

if __name__ == "__main__":
    grid1 = [[1,3],[2,2]]
    grid2 = [[9,1,7],[8,9,2],[3,4,6]]
    print(findMissingAndRepeatedValues(grid1))
    print(findMissingAndRepeatedValues(grid2))