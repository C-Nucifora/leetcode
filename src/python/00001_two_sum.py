# id: 00001
# difficulty: easy
# tags: array, hash_table
# url: https://leetcode.com/problems/two-sum
# time: O(n)
# space: O(n)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen = {}  # Val: Pos
        i = 0
        for i in range(len(nums)):
            required = target - nums[i]
            if required in seen:  # We have seen it before
                return [seen[required], i]

            seen[nums[i]] = i

        return []
