/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function (nums) {
  let ans = nums[0];
  let tmp = 0;
  for (const i of nums) {
    tmp = Math.max(tmp + i, i);
    ans = Math.max(ans, tmp);
  }
  return ans;
};
