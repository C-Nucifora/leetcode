# id: 0009
# difficulty: easy
# tags: math
# url: https://leetcode.com/problems/palindrome-number
# time: O(n)
# space: O(1)

class Solution:
    def isPalindrome(self, x: int) -> bool:

        original = x
        rev = 0

        while x > 0:
            rev = rev*10 + x % 10
            x = x//10

        return rev == original
