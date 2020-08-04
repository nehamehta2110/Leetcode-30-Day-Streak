class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        count = 0
        for i in range(0, len(nums)):
            if nums[i] != 0:
                nums[count], nums[i] = nums[i], nums[count]
                count += 1


def main():
    solve = Solution()
    solve.moveZeroes([1, 3, 0, 6, 0, 12])


if __name__ == '__main__':
    main()
