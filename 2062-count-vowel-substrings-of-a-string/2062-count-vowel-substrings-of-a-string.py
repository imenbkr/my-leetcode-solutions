class Solution(object):
    def countVowelSubstrings(self, word):
        """
        :type word: str
        :rtype: int
        """
        word = word.lower()
        count=0
        for i in range (len(word)):
            for j in range (i, len(word)):
                if set(word[i:j+1]) == set("aeiou"):
                    count+=1
        return count