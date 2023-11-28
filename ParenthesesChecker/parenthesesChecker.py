#Parentheses Checker Problem

#time complexity - O(n)
def parenthesesChecker(str):
    stack = []
    mapping = {')' : '(', '}' : '{', ']' : '['}

    for char in str:
        if char in mapping.values():
            stack.append(char)

        elif char in mapping:
            if not stack or stack.pop() != mapping[char]:
                return False
            
    return not stack

if __name__ == "__main__":
    string = "{[([])]}"
    print(parenthesesChecker(string))
