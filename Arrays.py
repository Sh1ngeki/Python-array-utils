class Solution(object):

    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return i, j

    def lengthOfLongestSubstring(self, s):
        char_set = set()
        max_length = 0
        left = 0
        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            max_length = max(max_length, right - left + 1)
        return max_length

    def maxProfit(self, prices):
        max_profit = 0
        min_price = float("inf")
        for price in prices:
            min_price = min(min_price, price)
            current = price - min_price
            max_profit = max(max_profit, current)
        return max_profit

    def containsDuplicate(self, nums):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False

    def productExceptSelf(self, nums):
        answers = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            answers[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            answers[i] *= suffix
            suffix *= nums[i]

        return answers

    def maxSubArray(self, nums):
        max_current = nums[0]
        max_sums = nums[0]

        for i in range(1, len(nums)):
            max_current = max(nums[i], max_current + nums[i])
            max_sums = max(max_sums, max_current)

        return max_sums
