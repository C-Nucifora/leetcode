# id: 00058
# difficulty: easy
# tags: string
# url: https://leetcode.com/problems/length-of-last-word/
# time: O(n)
# space: O(n)

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        final_word = s.split()[-1]

        return len(final_word)
