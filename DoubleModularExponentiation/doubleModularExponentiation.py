#Double Modular Exponentiation
#time complexity - of O(n), where n is the length of the variables list
def getGoodIndices(variables, target):
    goodIndices = []
    
    for i, var in enumerate(variables):
        a, b, c, m = var

        if (((a**b) % 10)**c) % m == target:
            goodIndices.append(i)

    return goodIndices

if __name__ == "__main__":
    variables = [[2,3,3,10],[3,3,3,1],[6,1,1,4]]
    target = 2
    print(getGoodIndices(variables, target))