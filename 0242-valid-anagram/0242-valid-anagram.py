class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s = s.lower()
        t = t.lower()
        
        temp=True
                
        if len(s)!= len(t):
            temp =False
            
        counter = {}
        for i in s :
            if i in counter.keys() :
                counter[i] += 1
            else: 
                counter[i] = 1
        
        counter2 = {}
        for j in t :
            if j in counter2.keys() :
                counter2[j] +=1
            else: 
                counter2[j] = 1
                
                
        if counter == counter2 :
            temp = True
        else: 
            temp= False
        
        return temp