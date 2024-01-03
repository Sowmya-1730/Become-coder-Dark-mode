#Problem of the day
class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        m=len(bank)
        n=len(bank[0])
        d=[]
        for i in bank:
            res=i.count('1')
            if res==0:
                d.append(0)
            else:
                d.append(res)
        res=0
        prev=0
        for i in d:
            if i:
                res+=prev*i
                prev=i
        if res==0:
            return 0
        else:
            return res
