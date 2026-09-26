class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for char in s:
            if char in '([{':
                stack.append(char)
            
            if not stack:
                return False

            if char == '}':
                if stack[-1]!='{':
                    return False
                stack.pop()
            
            if char == ']':
                if stack[-1]!='[':
                    return False
                stack.pop()

            if char == ')':
                if stack[-1]!='(':
                    return False
                stack.pop()

        return not stack
        