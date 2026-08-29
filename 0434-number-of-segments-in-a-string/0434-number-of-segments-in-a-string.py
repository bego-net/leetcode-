class Solution:
    def countSegments(self, s: str) -> int:
        c=0
        s=s.split(" ")
        for i in range(len(s)):
            if s[i]!="":
                c+=1
     
        return c
        