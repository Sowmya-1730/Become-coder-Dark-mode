class Solution:
    def repeatedCharacter(self, s: str) -> str:
        d={}
        for i in str:
            if i in d.keys():
                return i
            else:
                d[i]=1
