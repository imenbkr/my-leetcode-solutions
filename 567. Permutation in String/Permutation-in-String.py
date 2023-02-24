from collections import Counter
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        """
        we have to find a substring in s2 such that the frequency of the characters 
        in that substring is same as the frequency of the characters in s1.
        """
        if len(s1)>len(s2): return False
        #we can do it with the sliding window method
        #initialize counters c1 and c2
        c1 = Counter(s1) #frequence of all characters in s1
        c2 = Counter() #start window
        #get size of s1
        size = len(s1)
        #iterate until end of the window reaches the end of s2.
        for index, char in enumerate(s2):
                c2[char]+=1
                #if index >= size of s1
                if (index >= size) :
                    #remove window
                        left_element = s2[index - size]
                        if c2[left_element]==1:
                            del c2[left_element]
                        else: 
                            c2[left_element]-=1
                #for loop until :
                #if counter of items of s1 == counter c2 
                #means all the items in c1 have the same count also in c2
                if c1 == c2:
                    return True
        return False
            
        #we can do it by brute force: search for all the permutations of s1 in s2
        """
        #get all permutations of s1:
        temp= list(s1.lower())
        permutations = list(itertools.permutations(temp))
        matches= [''.join(permutation) for permutation in permutations]
        #if any of permutations are found in s2 return True
        if any([x in s2 for x in matches]):
            return True
        return False
        """
        #this method gives a 'time limit exceeded' error