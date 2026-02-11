from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
           n = len(nums)

           for i in range(n):
                 for j in range(i + 1, n):
                      if nums[i] + nums[j] == target:
                           return [i, j]

nums = [3, 2, 4]
target = 6
print(Solution().twoSum(nums, target))