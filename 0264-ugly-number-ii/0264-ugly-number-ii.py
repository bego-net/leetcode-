class Solution:
    def nthUglyNumber(self, n: int) -> int:
        list1=[0]*n
        list1[0]=1
        a=b=c=0
        for i in range(1,n):
            list1[i]=min(list1[a]*2,list1[b]*3,list1[c]*5)
            if list1[a]*2==list1[i]:a+=1
            if list1[b]*3==list1[i]:b+=1
            if list1[c]*5==list1[i]:c+=1
        return list1[n-1]
        
    #please upvote me it would encourage me alot