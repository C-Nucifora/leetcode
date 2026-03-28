# id: 01162
# difficulty: easy
# tags: array, string
# url: https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent
# time: O(n + m)
# space: O(n + m)


class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        string1, string2 = '', ''

        for i in range(len(word1)):
            string1 += word1[i]
        for i in range(len(word2)):
            string2 += word2[i]

        return string1 == string2
