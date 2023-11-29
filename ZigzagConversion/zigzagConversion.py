#Zigzag Conversion 
#Time Complexity - O(n) where n is the length of string

def zigzagConversion(s, numRows) -> str:
    rows = [''] * numRows
    index, step = 0, 1
    
    for char in s:
        rows[index] += char
        
        if index == 0:
            step = 1
        
        if index == numRows - 1:
            step = -1
            
        index += step
        
    return ''.join(rows)

if __name__ == "__main__":
    s = "PAYPALISHIRING"
    numRows = 4 
    res = zigzagConversion(s, numRows)
    print(res)
    
    
    
