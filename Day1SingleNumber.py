"""
Given a non-empty array of integers, every element appears twice except for one. Find that single one.
"""


class Solution:

    def singleNumber(self, nums):

        sum1 = sum2 = 0
        for i in nums:
            sum1 += i

        num = list(set(nums))

        for i in num:
            sum2 += 2 * i

        return sum2 - sum1


def main():
    sol = Solution()
    A = [2, 2, 1, 4, 4]
    print(sol.singleNumber(A))


if __name__ == '__main__':
    main()
