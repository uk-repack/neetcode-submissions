class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ## prefix and postfix optimal solution
        res = [1] * len(nums) # Because multiplication identity is 1.

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            # update prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res