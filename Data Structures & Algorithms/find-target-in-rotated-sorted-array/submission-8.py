class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # if len(nums) == 1:
        #     if nums[0] == target:
        #         return 0
        #     else:
        #         return -1
        
        # Find the new rotated point
        l, r = 0, len(nums) - 1
    
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[l]:
                l = mid
            else:
                r = mid
        
        pivot = r   

        print(pivot)
        def binary_search(l, r):
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
            return -1
        
        res = binary_search(0, pivot)
        if res != -1:
            return res
        return binary_search(pivot + 1, len(nums) - 1)

        