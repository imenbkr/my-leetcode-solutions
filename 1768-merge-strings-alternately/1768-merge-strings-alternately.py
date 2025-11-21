class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n= len(word1)-1
        m= len(word2)-1
        i=0
        merged=""
        len_merged = min(n, m)
        while(i <= len_merged):
            merged += word1[i]+word2[i]
            i+=1

        if n<m:
            merged+=word2[i:]
        else:
            merged+=word1[i:]

        return merged
