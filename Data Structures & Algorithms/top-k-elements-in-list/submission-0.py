# REDO THIS ONE
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}

        for n in nums:
            if n not in counts.keys():
                counts[n] = 1
            else:
                counts[n] += 1
        
        freq = [[] for i in range(len(nums) + 1)]

        for n, v in counts.items():
            freq[v].append(n)

        res = []
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
        
        return res
            
