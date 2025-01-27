# Longest Prefix
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        strs.sort()
        s=''
        first=strs[0]
        last=strs[-1]
        for i in range(len(first)):
            if first[i] !=last[i]:
                break
            else:
                s+=first[i]
        return s

