class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        
        for i in range(0, len(nums)):
            prod = 1 # reset product as 1 every time
            for j in range(0, len(nums)):
                if i != j: # compare indices
                    prod = prod * nums[j]
            res.append(prod)
        return res
            