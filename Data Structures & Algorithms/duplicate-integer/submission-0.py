class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        remove_dup = set(nums)
        if len(remove_dup) != len(nums):
            return True
        
        return False
         