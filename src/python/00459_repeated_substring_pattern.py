# id: 00459
# difficulty: easy
# tags: string, string_matching
# url: https://leetcode.com/problems/repeated-substring-pattern/
# time: O(n^2) worst-case, O(n) average-case
# space: O(n)


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        duplicated_string = s * 2
        duplicated_string = duplicated_string[1:-1]

        if s in duplicated_string:
            return True
        else:
            return False
