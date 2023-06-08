class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
                
        values = {}
        for i, value in enumerate(numbers):
            if target - value in values:
                return [values[target - value], i+1]
            else:
                values[value] = i+1
