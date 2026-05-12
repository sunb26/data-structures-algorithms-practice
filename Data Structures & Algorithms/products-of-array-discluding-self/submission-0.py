class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # This problem uses prefix AND postfix array to account for not using the division operator
        # The prefix product up until a particular index multiplied by the postfix up until that
        # index will be the product of the whole array except that index!

        res = []

        prefix = 1
        for i in range(len(nums)):
            res.append(prefix)
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        
        return res

            
