class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = nums[0]
        tmp = 0
        for i in nums:
            tmp = max(tmp+i, i)
            ans = max(tmp, ans)
        return ans
