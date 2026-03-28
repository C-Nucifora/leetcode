# id: 00674
# difficulty: easy
# tags: array
# url: https://leetcode.com/problems/longest-continuous-increasing-subsequence
# time: O(n)
# space: O(1)

class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:

        current_string = 1
        longest_string = -1

        for num in range(len(nums) - 1):
            if nums[num] >= nums[num + 1]:
                current_string = 1
            else:
                print('else')
                current_string += 1

            if current_string >= longest_string:
                longest_string = current_string

        if longest_string == -1:
            longest_string = 1
        return longest_string
