# id: 00678
# difficulty: medium
# tags: string, dynamic programming, stack, greedy
# url: https://leetcode.com/problems/valid-parenthesis-string
# time: O(n)
# space: O(1)

class Solution:
    def checkValidString(self, s: str) -> bool:
        left_min = 0
        left_max = 0

        for val in s:

            if val == '(':
                left_min += 1
                left_max += 1
            elif val == ')':
                left_min -= 1
                left_max -= 1
            else:
                left_min -= 1
                left_max += 1

            if left_max < 0:
                return False

            if left_min < 0:
                left_min = 0

        return left_min == 0
