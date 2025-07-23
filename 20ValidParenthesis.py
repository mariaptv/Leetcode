class validParenthesis:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i == '(' or i == '{' or i == '[':
                stack.append(i)
            elif i == ')' and stack and stack[-1] == '(':
                stack.pop()
            elif i == '}' and stack and stack[-1] == '{':
                stack.pop()
            elif i == ']' and stack and stack[-1] == '[':
                stack.pop()
            else:
                return False
        return len(stack) == 0
# Example usage:

new = validParenthesis()
print(new.isValid("()[]"))  # Output: True
# Return the count of unique elements, which is k +