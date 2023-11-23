class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dic1 = {}
        dic2 = {}
        for _ in range(len(s)):
            c = s[_]
            if c in dic1:
                dic1[c] +=1
            else:
                dic1[c] = 1

        for _ in range(len(t)): #t
            c = s[_]
            if c in dic2:
                dic2[c] +=1
            else:
                dic2[c] = 1


        for i in range(len(s)):
            c = s[i]
            if dic1.get(c,-2) != dic2.get(c,-1):
                return False
        return True