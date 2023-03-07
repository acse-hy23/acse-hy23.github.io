function maxSubArray(nums: number[]): number {
    let ans: number = nums[0];
    let tmp: number = 0
    for (const i of nums) {
        tmp = Math.max(tmp + i, i);
        ans = Math.max(ans, tmp);
    }
    return ans;
};