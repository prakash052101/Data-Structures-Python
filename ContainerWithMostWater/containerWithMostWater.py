#Container with most water
#time complexity - O(n), where n is the number of elements in the input array height

def maxArea(height):
    max_area = 0
    i, j = 0, len(height) - 1
    
    while i < j:
        h1 = height[i]
        h2 = height[j]
        
        width = j - i
        area = (h1 if h1 < h2 else h2) * width          #min(h1, h2) * width
        
        max_area = area if area > max_area else max_area    #max(area, max_area)
        
        if h1 < h2:
            i += 1
        else:
            j -= 1
        
    return max_area


if __name__ == "__main__":
    height = [1,8,6,2,5,4,8,3,7]
    res = maxArea(height)
    print(res)
