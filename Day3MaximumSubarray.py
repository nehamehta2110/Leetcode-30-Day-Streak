"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
Example:
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
"""


class Solution:
    def __init__(self, nums):
        self.nums = nums

    def maxSubArray(self):
        max_so_far = self.nums[0]
        curr_max = self.nums[0]

        for i in range(1, len(self.nums)):
            curr_max = max(self.nums[i], curr_max + self.nums[i])
            max_so_far = max(max_so_far, curr_max)

        return max_so_far


def main():
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    solve = Solution(nums)
    print(solve.maxSubArray())


if __name__ == '__main__':
    main()
