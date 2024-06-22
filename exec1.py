# pylint: disable=C0114,C0115,C0116,C0103
# pylint: disable=W0621
# https://leetcode.com/problems/two-sum/


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list:
        count = len(nums)
        for i in range(0, count - 1):
            for j in range(i + 1, count):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return None

    def twoSum2(self, nums: list, target: int) -> list:
        m = {}
        for i, num in enumerate(nums):
            t = target - num
            if t in m:
                return [i, m[t]]

            m[num] = i

        return None


if __name__ == "__main__":

    s = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    print(s.twoSum2(nums, target))
