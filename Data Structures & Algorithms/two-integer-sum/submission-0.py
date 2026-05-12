class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}

        for i in range(len(nums)):
            newTarget = target - nums[i]
            if newTarget in hashMap.keys():
                return hashMap[newTarget], i
            hashMap[nums[i]] = i

        