class Solution:
    def isPalindrome(self, s: str) -> bool:
        length = len(s)
        point1 = 0
        point2 = length - 1
        while point1 < point2:
            while point1 < point2 and not self.alphaNum(s[point1]):
                point1 += 1
            while point2 > point1 and not self.alphaNum(s[point2]):
                point2 -= 1
            if s[point1].lower() != s[point2].lower():
                return False
            else:
                point1 += 1
                point2 -= 1
        return True
            

    def alphaNum(self, c):
        return (ord("A") <= ord(c) <= ord("Z")
        or ord("a") <= ord(c) <= ord("z")
        or ord("0") <= ord(c) <= ord("9")
        )
        