from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        start, i = 0, 0
        end = len(nums) - 1
        while i < len(nums):
            if i > end:
                break
            if nums[i] == 2:
                nums[i], nums[end] = nums[end], nums[i]
                end -= 1
                i -= 1

            elif nums[i] == 0:
                nums[i], nums[start] = nums[start], nums[i]
                start += 1
            i += 1