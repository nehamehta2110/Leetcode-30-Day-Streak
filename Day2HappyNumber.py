"""
A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.
Return True if n is a happy number, and False if not.
Example:
Input: 19
Output: true
"""


class Solution:

    def isHappy(self, n):
        s = set()
        s.add(n)

        while True:

            if n == 1:
                return True

            sq_sum = 0

            while n:
                sq_sum += (n % 10) * (n % 10)
                n = n // 10
            n = sq_sum

            print(sq_sum)

            if n in s:
                return False

            s.add(n)

        return False


def main():
    sol = Solution()
    print(sol.isHappy(19))


if __name__ == '__main__':
    main()
