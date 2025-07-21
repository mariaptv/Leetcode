class Palindrome:
    def palindrome(self, x: int) -> bool:
        if x < 0:
            return False
        lx = list(map(int, str(x)))
        rev = lx.reverse()
        if lx == list(reversed(lx)):
            return True
        else:
            return False
        
# Example usage:
if __name__ == "__main__":
    p = Palindrome()
    print(p.palindrome(121))  # Output: True
    print(p.palindrome(-121)) # Output: False
    print(p.palindrome(10))   # Output: False
    print(p.palindrome(12321)) # Output: True    python3 Leetcode/9Palindrome.py