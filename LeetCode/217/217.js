/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function (nums) {
  const hashset = new Set();
  for (const num of nums) {
    if (hashset.has(num)) {
      return true;
    }
    hashset.add(num);
  }
  return false;
};
