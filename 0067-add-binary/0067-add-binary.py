class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        i, j = len(a) - 1, len(b) - 1
        carry = 0
        result = []
        
        while i >= 0 or j >= 0 or carry:
            digit_a = int(a[i]) if i >= 0 else 0
            digit_b = int(b[j]) if j >= 0 else 0
            
            total = digit_a + digit_b + carry
            carry = total // 2  # New carry is the integer division by 2
            result.append(str(total % 2))  # Append the remainder (0 or 1) to the result

            i -= 1
            j -= 1
        
        return ''.join(reversed(result))