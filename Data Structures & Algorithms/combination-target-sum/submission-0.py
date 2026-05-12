class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        
        #dfs

        def dfs(combo, curr_sum, i):
            
            if i >= len(nums) or curr_sum > target:
                return
            
            if curr_sum == target:
                res.append(combo.copy())
                return
                
            combo.append(nums[i])
            dfs(combo, sum(combo), i)
            combo.pop()
            dfs(combo, sum(combo), i + 1)
        

        dfs([], 0, 0)

        return res