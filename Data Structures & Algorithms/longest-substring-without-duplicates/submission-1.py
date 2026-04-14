class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dicti = {}
        l = 0
        r = 0
        maxi = 0
        if len(s) == 0:
            return maxi
        while 1:
            print(l, r)
            if s[r] not in dicti and r + 1 < len(s):
                length = r - l + 1
                if length > maxi:
                    maxi = length
                dicti[s[r]] = 1
                r += 1
            elif s[r] not in dicti and r + 1 == len(s):
                length = r - l + 1
                if length > maxi:
                    maxi = length
                return maxi
            else:
                while (1):
                    if s[l] != s[r]:
                        dicti.pop(s[l])
                        l += 1
                    else:
                        dicti.pop(s[l])
                        l += 1
                        break
        