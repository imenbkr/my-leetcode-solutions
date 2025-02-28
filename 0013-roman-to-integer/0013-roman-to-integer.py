class Solution:
    def romanToInt(self, s: str) -> int:
        d={'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        prev, result = 0,0

        for i in range(len(s)-1, -1, -1):
            #example : s="MCMXCIV"
            curr = d[s[i]] #get current value of roman number #d['M']=1000
            if prev > curr:
                result-=curr #994
            else:
                result+=curr #1994
            prev = curr #100

        return result
            