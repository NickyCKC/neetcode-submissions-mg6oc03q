class Solution:
    def isValid(self, s: str) -> bool:
        length = len(s)
        if length % 2 != 0:
            print("error 1")
            return False
        stack = []
        dicti = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }
        for char in s:
            if char in dicti:
                if stack and dicti[char] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        if not stack:
            return True
        else:
            return False
            

        