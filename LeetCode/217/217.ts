function containsDuplicate(nums: number[]): boolean {
    const hashset = new Set<number>();
    for (const i of nums) {
        if (hashset.has(i)) {
            return true;
        }
        hashset.add(i);
    }
    return false;
};