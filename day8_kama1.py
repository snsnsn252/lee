# kamaCode
# https://kamacoder.com/problempage.php?pid=1064

class Solution:
    def replaceNumber(self,s:str)->str:
        count = 0
        for char in s: 
            if char.isdigit():
                count += 1 
        
        n = len(s) - 1 + 5 * count  # five additional position for each count
        
        i = len(s) - 1  # old last position
        j = n   # new last position 
        
        res = [0] * (n + 1)
        while i >= 0:
            if not s[i].isdigit():
                res[j] = s[i]
            else:
                res[j] = 'r'
                res[j-1] = 'e'
                res[j-2] = 'b'
                res[j-3] = 'm'
                res[j-4] = 'u'
                res[j-5] = 'n'
                j -= 5
            i -= 1 
            j -= 1 
        return ''.join(res)

sol = Solution()
s = input()
result = sol.replaceNumber(s)
print(result)